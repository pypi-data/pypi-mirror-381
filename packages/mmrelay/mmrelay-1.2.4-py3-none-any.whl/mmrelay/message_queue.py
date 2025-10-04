"""
Message queue system for MMRelay.

Provides transparent message queuing with rate limiting to prevent overwhelming
the Meshtastic network. Messages are queued in memory and sent at the configured
rate, respecting connection state and firmware constraints.
"""

import asyncio
import contextlib
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from functools import partial
from queue import Empty, Full, Queue
from typing import Callable, Optional

from mmrelay.constants.database import DEFAULT_MSGS_TO_KEEP
from mmrelay.constants.network import MINIMUM_MESSAGE_DELAY
from mmrelay.constants.queue import (
    DEFAULT_MESSAGE_DELAY,
    MAX_QUEUE_SIZE,
    QUEUE_HIGH_WATER_MARK,
    QUEUE_MEDIUM_WATER_MARK,
)
from mmrelay.log_utils import get_logger

logger = get_logger(name="MessageQueue")


@dataclass
class QueuedMessage:
    """Represents a message in the queue with metadata."""

    timestamp: float
    send_function: Callable
    args: tuple
    kwargs: dict
    description: str
    # Optional message mapping information for replies/reactions
    mapping_info: Optional[dict] = None


class MessageQueue:
    """
    Simple FIFO message queue with rate limiting for Meshtastic messages.

    Queues messages in memory and sends them in order at the configured rate to prevent
    overwhelming the mesh network. Respects connection state and automatically
    pauses during reconnections.
    """

    def __init__(self):
        """
        Create a new MessageQueue, initializing its internal queue, timing and state variables, and a thread lock.

        Attributes:
            _queue (Queue): Bounded FIFO holding queued messages (maxsize=MAX_QUEUE_SIZE).
            _processor_task (Optional[asyncio.Task]): Async task that processes the queue, created when started.
            _running (bool): Whether the processor is active.
            _lock (threading.Lock): Protects start/stop and other state transitions.
            _last_send_time (float): Wall-clock timestamp of the last successful send.
            _last_send_mono (float): Monotonic timestamp of the last successful send (used for rate limiting).
            _message_delay (float): Minimum delay between sends; starts at DEFAULT_MESSAGE_DELAY and may be adjusted.
            _executor (Optional[concurrent.futures.ThreadPoolExecutor]): Dedicated single-worker executor for blocking send operations (created on start).
            _in_flight (bool): True while a message send is actively running in the executor.
            _has_current (bool): True when there is a current message being processed (even if not yet dispatched to the executor).
        """
        self._queue = Queue(maxsize=MAX_QUEUE_SIZE)
        self._processor_task = None
        self._running = False
        self._lock = threading.Lock()
        self._last_send_time = 0.0
        self._last_send_mono = 0.0
        self._message_delay = DEFAULT_MESSAGE_DELAY
        self._executor = None  # Dedicated ThreadPoolExecutor for this MessageQueue
        self._in_flight = False
        self._has_current = False
        self._dropped_messages = 0

    def start(self, message_delay: float = DEFAULT_MESSAGE_DELAY):
        """
        Activate the message queue processor with a minimum inter-message delay.

        Enables processing, sets the configured message delay (raised to MINIMUM_MESSAGE_DELAY if a smaller value is provided), creates a dedicated ThreadPoolExecutor for send operations if one does not exist, and starts the asyncio processor task immediately when a running event loop is available; if no running loop is available startup is deferred until a loop is present.

        Parameters:
            message_delay (float): Requested minimum delay between sends, in seconds. Values below MINIMUM_MESSAGE_DELAY are replaced with MINIMUM_MESSAGE_DELAY.
        """
        with self._lock:
            if self._running:
                return

            # Validate and enforce firmware minimum
            if message_delay < MINIMUM_MESSAGE_DELAY:
                logger.warning(
                    f"Message delay {message_delay}s below firmware minimum ({MINIMUM_MESSAGE_DELAY}s), using {MINIMUM_MESSAGE_DELAY}s"
                )
                self._message_delay = MINIMUM_MESSAGE_DELAY
            else:
                self._message_delay = message_delay
            self._running = True

            # Create dedicated executor for this MessageQueue
            if self._executor is None:
                self._executor = ThreadPoolExecutor(
                    max_workers=1, thread_name_prefix=f"MessageQueue-{id(self)}"
                )

            # Start the processor in the event loop
            try:
                try:
                    loop = asyncio.get_running_loop()
                except RuntimeError:
                    loop = None
                if loop and loop.is_running():
                    self._processor_task = loop.create_task(self._process_queue())
                    logger.info(
                        f"Message queue started with {self._message_delay}s message delay"
                    )
                else:
                    # Event loop exists but not running yet, defer startup
                    logger.debug(
                        "Event loop not running yet, will start processor later"
                    )
            except RuntimeError:
                # No event loop running, will start when one is available
                logger.debug(
                    "No event loop available, queue processor will start later"
                )

    def stop(self):
        """
        Stop the message queue processor and clean up internal resources.

        Cancels the background processor task (if running) and attempts to wait for it to finish on the task's owning event loop without blocking the caller's event loop. Shuts down the dedicated ThreadPoolExecutor used for blocking I/O; when called from an asyncio event loop the executor shutdown is performed on a background thread to avoid blocking. Clears internal state flags and resources so the queue can be restarted later.

        Notes:
        - This method is thread-safe.
        - It may block briefly (the implementation waits up to ~1 second when awaiting task completion) but will avoid blocking the current asyncio event loop when possible.
        - No exceptions are propagated for normal cancellation/shutdown paths; internal exceptions during shutdown are suppressed.
        """
        with self._lock:
            if not self._running:
                return

            self._running = False

            if self._processor_task:
                self._processor_task.cancel()

                # Wait for the task to complete on its owning loop
                task_loop = self._processor_task.get_loop()
                current_loop = None
                with contextlib.suppress(RuntimeError):
                    current_loop = asyncio.get_running_loop()
                if task_loop.is_closed():
                    # Owning loop is closed; nothing we can do to await it
                    pass
                elif current_loop is task_loop:
                    # Avoid blocking the event loop thread; cancellation will finish naturally
                    pass
                elif task_loop.is_running():
                    from asyncio import run_coroutine_threadsafe, shield

                    with contextlib.suppress(Exception):
                        fut = run_coroutine_threadsafe(
                            shield(self._processor_task), task_loop
                        )
                        # Wait for completion; ignore exceptions raised due to cancellation
                        fut.result(timeout=1.0)
                else:
                    with contextlib.suppress(
                        asyncio.CancelledError, RuntimeError, Exception
                    ):
                        task_loop.run_until_complete(self._processor_task)

                self._processor_task = None

            # Shut down our dedicated executor without blocking the event loop
            if self._executor:
                on_loop_thread = False
                with contextlib.suppress(RuntimeError):
                    loop_chk = asyncio.get_running_loop()
                    on_loop_thread = loop_chk.is_running()

                def _shutdown(exec_ref):
                    """
                    Shut down an executor, waiting for running tasks to finish; falls back for executors that don't support `cancel_futures`.

                    Attempts to call executor.shutdown(wait=True, cancel_futures=True) and, if that raises a TypeError (older Python versions or executors without the `cancel_futures` parameter), retries with executor.shutdown(wait=True). This call blocks until shutdown completes.
                    """
                    try:
                        exec_ref.shutdown(wait=True, cancel_futures=True)
                    except TypeError:
                        exec_ref.shutdown(wait=True)

                if on_loop_thread:
                    threading.Thread(
                        target=_shutdown,
                        args=(self._executor,),
                        name="MessageQueueExecutorShutdown",
                        daemon=True,
                    ).start()
                else:
                    _shutdown(self._executor)
                self._executor = None

            logger.info("Message queue stopped")

    def enqueue(
        self,
        send_function: Callable,
        *args,
        description: str = "",
        mapping_info: Optional[dict] = None,
        **kwargs,
    ) -> bool:
        """
        Enqueue a message for ordered, rate-limited sending.

        Ensures the queue processor is started (if an event loop is available) and attempts to add a QueuedMessage (containing the provided send function and its arguments) to the bounded in-memory queue. If the queue is not running or has reached capacity the message is not added and the method returns False. Optionally attach mapping_info metadata (used later to correlate sent messages with external IDs).

        Parameters:
            send_function (Callable): Callable to execute when the message is sent.
            *args: Positional arguments to pass to send_function.
            description (str, optional): Human-readable description used for logging.
            mapping_info (dict | None, optional): Optional metadata to record after a successful send.
            **kwargs: Keyword arguments to pass to send_function.

        Returns:
            bool: True if the message was successfully enqueued; False if the queue is not running or is full.
        """
        # Ensure processor is started if event loop is now available.
        # This is called outside the lock to prevent potential deadlocks.
        self.ensure_processor_started()

        with self._lock:
            if not self._running:
                # Refuse to send to prevent blocking the event loop
                logger.error(
                    "Queue not running; cannot send message: %s. Start the message queue before sending.",
                    description,
                )
                return False

            message = QueuedMessage(
                timestamp=time.time(),
                send_function=send_function,
                args=args,
                kwargs=kwargs,
                description=description,
                mapping_info=mapping_info,
            )
            # Enforce capacity via bounded queue
            try:
                self._queue.put_nowait(message)
            except Full:
                logger.warning(
                    f"Message queue full ({self._queue.qsize()}/{MAX_QUEUE_SIZE}), dropping message: {description}"
                )
                self._dropped_messages += 1
                return False
            # Only log queue status when there are multiple messages
            queue_size = self._queue.qsize()
            if queue_size >= 2:
                logger.debug(
                    f"Queued message ({queue_size}/{MAX_QUEUE_SIZE}): {description}"
                )
            return True

    def get_queue_size(self) -> int:
        """
        Return the number of messages currently in the queue.

        Returns:
            int: The current queue size.
        """
        return self._queue.qsize()

    def is_running(self) -> bool:
        """
        Return whether the message queue processor is currently active.
        """
        return self._running

    def get_status(self) -> dict:
        """
        Return current status of the message queue.

        Provides a snapshot useful for monitoring and debugging.

        Returns:
            dict: Mapping with the following keys:
                - running (bool): Whether the queue processor is active.
                - queue_size (int): Number of messages currently queued.
                - message_delay (float): Configured minimum delay (seconds) between sends.
                - processor_task_active (bool): True if the internal processor task exists and is not finished.
                - last_send_time (float or None): Wall-clock time (seconds since the epoch) of the last successful send, or None if no send has occurred.
                - time_since_last_send (float or None): Seconds elapsed since last_send_time, or None if no send has occurred.
                - in_flight (bool): True when a message is currently being sent.
                - dropped_messages (int): Number of messages dropped due to queue being full.
                - default_msgs_to_keep (int): Default retention setting for message mappings.
        """
        return {
            "running": self._running,
            "queue_size": self._queue.qsize(),
            "message_delay": self._message_delay,
            "processor_task_active": self._processor_task is not None
            and not self._processor_task.done(),
            "last_send_time": self._last_send_time,
            "time_since_last_send": (
                time.monotonic() - self._last_send_mono
                if self._last_send_mono > 0
                else None
            ),
            "in_flight": self._in_flight,
            "dropped_messages": getattr(self, "_dropped_messages", 0),
            "default_msgs_to_keep": DEFAULT_MSGS_TO_KEEP,
        }

    async def drain(self, timeout: Optional[float] = None) -> bool:
        """
        Asynchronously wait until the queue has fully drained (no queued messages and no in-flight or current message) or until an optional timeout elapses.

        If `timeout` is provided, it is interpreted in seconds. Returns True when the queue is empty and there are no messages being processed; returns False if the queue was stopped before draining or the timeout was reached.
        """
        deadline = (time.monotonic() + timeout) if timeout is not None else None
        while (not self._queue.empty()) or self._in_flight or self._has_current:
            if not self._running:
                return False
            if deadline is not None and time.monotonic() > deadline:
                return False
            await asyncio.sleep(0.1)
        return True

    def ensure_processor_started(self):
        """
        Start the queue processor task if the queue is running and no processor task exists.

        This method checks if the queue is active and, if so, attempts to create and start the asynchronous processor task within the current event loop.
        """
        with self._lock:
            if self._running and self._processor_task is None:
                try:
                    loop = asyncio.get_running_loop()
                except RuntimeError:
                    loop = None
                if loop and loop.is_running():
                    self._processor_task = loop.create_task(self._process_queue())
                    logger.info(
                        f"Message queue processor started with {self._message_delay}s message delay"
                    )

    async def _process_queue(self):
        """
        Process queued messages in FIFO order, sending each when the connection is ready and the configured inter-message delay has elapsed.

        This background coroutine continuously pulls QueuedMessage items from the internal queue and executes their send_function in the configured executor, enforcing rate limiting (_message_delay) and checking connection/readiness via _should_send_message. After a successful send, it updates last-send timestamps and optionally persists message mapping information via _handle_message_mapping when mapping_info is present and the send result exposes an `id`. The coroutine exits when the queue is stopped or when cancelled; cancellation may drop an in-flight message, which will be logged.
        """
        logger.debug("Message queue processor started")
        current_message = None

        while self._running:
            try:
                # Get next message if we don't have one waiting
                if current_message is None:
                    # Monitor queue depth for operational awareness
                    queue_size = self._queue.qsize()
                    if queue_size > QUEUE_HIGH_WATER_MARK:
                        logger.warning(
                            f"Queue depth high: {queue_size} messages pending"
                        )
                    elif queue_size > QUEUE_MEDIUM_WATER_MARK:
                        logger.info(
                            f"Queue depth moderate: {queue_size} messages pending"
                        )

                    # Get next message (non-blocking)
                    try:
                        current_message = self._queue.get_nowait()
                        self._has_current = True
                    except Empty:
                        # No messages, wait a bit and continue
                        await asyncio.sleep(0.1)
                        continue

                # Check if we should send (connection state, etc.)
                if not self._should_send_message():
                    # Keep the message and wait - don't requeue to maintain FIFO order
                    logger.debug(
                        f"Connection not ready, waiting to send: {current_message.description}"
                    )
                    await asyncio.sleep(1.0)
                    continue

                # Check if we need to wait for message delay (only if we've sent before)
                if self._last_send_mono > 0:
                    time_since_last = time.monotonic() - self._last_send_mono
                    if time_since_last < self._message_delay:
                        wait_time = self._message_delay - time_since_last
                        logger.debug(
                            f"Rate limiting: waiting {wait_time:.1f}s before sending"
                        )
                        await asyncio.sleep(wait_time)
                        continue

                # Send the message
                try:
                    self._in_flight = True
                    logger.debug(
                        f"Sending queued message: {current_message.description}"
                    )
                    # Run synchronous Meshtastic I/O operations in executor to prevent blocking event loop
                    loop = asyncio.get_running_loop()
                    exec_ref = self._executor
                    if exec_ref is None:
                        raise RuntimeError("MessageQueue executor is not initialized")
                    result = await loop.run_in_executor(
                        exec_ref,
                        partial(
                            current_message.send_function,
                            *current_message.args,
                            **current_message.kwargs,
                        ),
                    )

                    # Update last send time
                    self._last_send_time = time.time()
                    self._last_send_mono = time.monotonic()

                    if result is None:
                        logger.warning(
                            f"Message send returned None: {current_message.description}"
                        )
                    else:
                        logger.debug(
                            f"Successfully sent queued message: {current_message.description}"
                        )

                        # Handle message mapping if provided
                        if current_message.mapping_info and hasattr(result, "id"):
                            self._handle_message_mapping(
                                result, current_message.mapping_info
                            )

                except Exception as e:
                    logger.error(
                        f"Error sending queued message '{current_message.description}': {e}"
                    )

                # Mark task as done and clear current message
                self._queue.task_done()
                current_message = None
                self._in_flight = False
                self._has_current = False

            except asyncio.CancelledError:
                logger.debug("Message queue processor cancelled")
                if current_message:
                    logger.warning(
                        f"Message in flight was dropped during shutdown: {current_message.description}"
                    )
                    with contextlib.suppress(Exception):
                        self._queue.task_done()
                self._in_flight = False
                self._has_current = False
                break
            except Exception:
                logger.exception("Error in message queue processor")
                await asyncio.sleep(1.0)  # Prevent tight error loop

    def _should_send_message(self) -> bool:
        """
        Check whether the queue may send a Meshtastic message.

        Performs runtime checks: returns True only if the reconnection flag is not set, a Meshtastic client object exists, and—if the client exposes `is_connected`—that check indicates the client is connected. If importing Meshtastic utilities raises ImportError, a critical log is emitted and the queue is stopped asynchronously.

        Returns:
            `True` if not reconnecting, a Meshtastic client exists, and the client is connected when checkable; `False` otherwise.
        """
        # Import here to avoid circular imports
        try:
            from mmrelay.meshtastic_utils import meshtastic_client, reconnecting

            # Don't send during reconnection
            if reconnecting:
                logger.debug("Not sending - reconnecting is True")
                return False

            # Don't send if no client
            if meshtastic_client is None:
                logger.debug("Not sending - meshtastic_client is None")
                return False

            # Check if client is connected
            if hasattr(meshtastic_client, "is_connected"):
                is_conn = meshtastic_client.is_connected
                if not (is_conn() if callable(is_conn) else is_conn):
                    logger.debug("Not sending - client not connected")
                    return False

            logger.debug("Connection check passed - ready to send")
            return True

        except ImportError as e:
            # ImportError indicates a serious problem with application structure,
            # often during shutdown as modules are unloaded.
            logger.critical(
                f"Cannot import meshtastic_utils - serious application error: {e}. Stopping message queue."
            )
            # Stop asynchronously to avoid blocking the event loop thread.
            threading.Thread(
                target=self.stop, name="MessageQueueStopper", daemon=True
            ).start()
            return False

    def _handle_message_mapping(self, result, mapping_info):
        """
        Persist a mapping from a sent Meshtastic message to a Matrix event and optionally prune old mappings.

        Stores a mapping when `mapping_info` contains `matrix_event_id`, `room_id`, and `text`, using `result.id` as the Meshtastic message id. If `mapping_info["msgs_to_keep"]` is present and greater than 0, prunes older mappings to retain that many entries; otherwise uses DEFAULT_MSGS_TO_KEEP.

        Parameters:
            result: An object returned by the send function with an `id` attribute representing the Meshtastic message id.
            mapping_info (dict): Mapping details. Relevant keys:
                - matrix_event_id (str): Matrix event ID to map to.
                - room_id (str): Matrix room ID where the event was sent.
                - text (str): Message text to associate with the mapping.
                - meshnet (optional): Mesh network identifier to pass to storage.
                - msgs_to_keep (optional, int): Number of mappings to retain when pruning.
        """
        try:
            # Import here to avoid circular imports
            from mmrelay.db_utils import prune_message_map, store_message_map

            # Extract mapping information
            matrix_event_id = mapping_info.get("matrix_event_id")
            room_id = mapping_info.get("room_id")
            text = mapping_info.get("text")
            meshnet = mapping_info.get("meshnet")

            if matrix_event_id and room_id and text:
                # Store the message mapping
                store_message_map(
                    result.id,
                    matrix_event_id,
                    room_id,
                    text,
                    meshtastic_meshnet=meshnet,
                )
                logger.debug(f"Stored message map for meshtastic_id: {result.id}")

                # Handle pruning if configured
                msgs_to_keep = mapping_info.get("msgs_to_keep", DEFAULT_MSGS_TO_KEEP)
                if msgs_to_keep > 0:
                    prune_message_map(msgs_to_keep)

        except Exception:
            logger.exception("Error handling message mapping")


# Global message queue instance
_message_queue = MessageQueue()


def get_message_queue() -> MessageQueue:
    """
    Return the global instance of the message queue used for managing and rate-limiting message sending.
    """
    return _message_queue


def start_message_queue(message_delay: float = DEFAULT_MESSAGE_DELAY):
    """
    Start the global message queue processor with the given minimum delay between messages.

    Parameters:
        message_delay (float): Minimum number of seconds to wait between sending messages.
    """
    _message_queue.start(message_delay)


def stop_message_queue():
    """
    Stops the global message queue processor, preventing further message processing until restarted.
    """
    _message_queue.stop()


def queue_message(
    send_function: Callable,
    *args,
    description: str = "",
    mapping_info: Optional[dict] = None,
    **kwargs,
) -> bool:
    """
    Enqueues a message for sending via the global message queue.

    Parameters:
        send_function (Callable): The function to execute for sending the message.
        description (str, optional): Human-readable description of the message for logging purposes.
        mapping_info (dict, optional): Additional metadata for message mapping, such as reply or reaction information.

    Returns:
        bool: True if the message was successfully enqueued; False if the queue is not running or full.
    """
    return _message_queue.enqueue(
        send_function,
        *args,
        description=description,
        mapping_info=mapping_info,
        **kwargs,
    )


def get_queue_status() -> dict:
    """
    Return detailed status information about the global message queue.

    Returns:
        dict: A dictionary containing the running state, queue size, message delay, processor task activity, last send time, and time since last send.
    """
    return _message_queue.get_status()
