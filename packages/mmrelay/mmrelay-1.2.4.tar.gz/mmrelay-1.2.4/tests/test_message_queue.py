#!/usr/bin/env python3
"""
Test suite for the MMRelay message queue system.

Tests the FIFO message queue functionality including:
- Message ordering (first in, first out)
- Rate limiting enforcement
- Connection state awareness
- Queue size limits
- Error handling
"""

import asyncio
import os
import sys
import time
import unittest

import pytest

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from mmrelay.constants.queue import MAX_QUEUE_SIZE
from mmrelay.message_queue import (
    MessageQueue,
    QueuedMessage,
    queue_message,
)


def mock_send_function(text, **kwargs):
    """
    Simulates sending a message and records the call details for testing purposes.

    Parameters:
        text (str): The message text to send.

    Returns:
        dict: A dictionary containing a unique 'id' for the sent message.
    """
    # This will be called synchronously due to executor mocking
    mock_send_function.calls.append(
        {"text": text, "kwargs": kwargs, "timestamp": time.time()}
    )
    return {"id": len(mock_send_function.calls)}


# Initialize calls list
mock_send_function.calls = []


class TestMessageQueue(unittest.TestCase):
    """Test cases for the MessageQueue class."""

    def setUp(self):
        """
        Set up test fixtures: initialize a MessageQueue, clear mock send records, force sending allowed, and create a dedicated asyncio event loop whose run_in_executor is patched to execute functions synchronously while returning an awaitable Future.

        Detailed behavior:
        - Creates a new MessageQueue assigned to self.queue.
        - Clears mock_send_function.calls.
        - Replaces self.queue._should_send_message with a lambda that returns True.
        - Creates a dedicated asyncio event loop, sets it as the current loop, and stores it on self.loop.
        - Saves the loop's original run_in_executor on self.original_run_in_executor.
        - Replaces run_in_executor with a synchronous wrapper that executes the supplied callable immediately and returns an asyncio.Future completed with the callable's result or exception, preserving the awaitable contract for tests.
        """
        self.queue = MessageQueue()
        # Clear mock function calls for each test
        mock_send_function.calls.clear()
        # Mock the _should_send_message method to always return True for tests
        self.queue._should_send_message = lambda: True

        # Use a dedicated event loop and patch run_in_executor to return an awaitable Future
        real_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(real_loop)
        self.loop = real_loop

        # Store original run_in_executor for restoration
        self.original_run_in_executor = real_loop.run_in_executor

        def sync_run_in_executor(executor, func, *args, **kwargs):
            """
            Run a callable synchronously but return an awaitable Future that is already completed with its result or exception.

            This preserves the awaitable contract expected by code that uses run_in_executor while executing the provided function synchronously on the current thread.

            Parameters:
                func (callable): Function to execute.
                *args: Positional arguments passed to `func`.
                **kwargs: Keyword arguments passed to `func`.

            Returns:
                asyncio.Future: A Future created on the test event loop and completed with `func`'s return value or raised exception.
            """
            fut = real_loop.create_future()
            try:
                res = func(*args, **kwargs)
                fut.set_result(res)
            except Exception as e:
                fut.set_exception(e)
            return fut

        real_loop.run_in_executor = sync_run_in_executor

    def tearDown(self):
        """
        Tear down test fixtures: stop the MessageQueue if running, restore the event loop's original run_in_executor, close the dedicated per-test loop, and clear the global event loop reference.

        This ensures the per-test asyncio loop created in setUp is properly shut down and any monkey-patched
        run_in_executor is restored. Suppresses errors when clearing the global event loop reference.
        """
        if self.queue.is_running():
            self.queue.stop()

        # Restore original run_in_executor and clean up the dedicated event loop created in setUp
        loop = getattr(self, "loop", None)
        if loop is not None:
            try:
                if hasattr(self, "original_run_in_executor"):
                    loop.run_in_executor = self.original_run_in_executor
                if not loop.is_closed():
                    loop.close()
            finally:
                import contextlib

                with contextlib.suppress(Exception):
                    asyncio.set_event_loop(None)

    @property
    def sent_messages(self):
        """
        Return the list of records for calls made to the test mock send function.

        Each list item is a dict-like record appended by the mock: it contains at least the sent text/payload, any kwargs, and a timestamp.
        """
        return mock_send_function.calls

    def test_fifo_ordering(self):
        """
        Verifies that the message queue sends messages in the order they were enqueued (FIFO).

        This test enqueues multiple messages, waits for them to be processed, and asserts that they are sent in the same order as they were added to the queue.
        """

        # Use asyncio to properly test the async queue
        async def async_test():
            # Start queue with fast rate for testing
            """
            Asynchronously tests that messages are processed and sent in FIFO order by the message queue.

            This test enqueues multiple messages, waits for them to be processed, and asserts that they are sent in the order they were enqueued.
            """
            self.queue.start(message_delay=0.1)

            # Ensure processor starts
            self.queue.ensure_processor_started()

            # Queue multiple messages (reduced for faster testing)
            messages = ["First", "Second", "Third"]
            for msg in messages:
                success = self.queue.enqueue(
                    mock_send_function,
                    text=msg,
                    description=f"Test message: {msg}",
                )
                self.assertTrue(success)

            # Wait for processing to complete with a timeout
            drained = await self.queue.drain(timeout=15.0)
            if not drained:
                self.fail(
                    f"Queue processing timed out. Sent {len(self.sent_messages)}/{len(messages)} messages, queue size: {self.queue.get_queue_size()}"
                )

            # Check that messages were sent in order
            self.assertEqual(len(self.sent_messages), len(messages))
            for i, expected_msg in enumerate(messages):
                self.assertEqual(self.sent_messages[i]["text"], expected_msg)

        # Run the async test on the dedicated loop so the patched executor is used
        self.loop.run_until_complete(async_test())

    def test_rate_limiting(self):
        """
        Verify that the message queue enforces rate limiting by delaying the sending of messages according to the configured interval.
        """

        async def async_test():
            """
            Verify the MessageQueue enforces rate limiting: when two messages are enqueued, the first is sent soon after processing starts and the second is delayed until the configured message_delay has elapsed.

            The test starts the queue with message_delay=2.1, enqueues two messages, then:
            - after ~1.0s asserts one message was sent,
            - after another ~1.0s asserts the second is still not sent,
            - after an additional ~1.5s asserts the second message has been sent.
            """
            message_delay = 2.1  # Use minimum message delay for testing
            self.queue.start(message_delay=message_delay)
            self.queue.ensure_processor_started()

            # Queue two messages
            self.queue.enqueue(mock_send_function, text="First")
            self.queue.enqueue(mock_send_function, text="Second")

            # Wait for first message
            await asyncio.sleep(1.0)
            self.assertEqual(len(self.sent_messages), 1)

            # Second message should not be sent yet (rate limit not passed)
            await asyncio.sleep(1.0)
            self.assertEqual(len(self.sent_messages), 1)

            # Wait for rate limit to pass
            await asyncio.sleep(1.5)
            self.assertEqual(len(self.sent_messages), 2)

        self.loop.run_until_complete(async_test())

    @pytest.mark.usefixtures("comprehensive_cleanup")
    def test_queue_size_limit(self):
        """
        Verify that the message queue enforces its maximum size limit by accepting messages up to the limit and rejecting additional messages beyond capacity.
        """
        # Start the queue but don't let it process (no event loop)
        self.queue._running = True  # Manually set running to prevent immediate sending

        # Fill queue to limit
        for i in range(MAX_QUEUE_SIZE):
            success = self.queue.enqueue(mock_send_function, text=f"Message {i}")
            self.assertTrue(success)

        # Next message should be rejected
        success = self.queue.enqueue(mock_send_function, text="Overflow message")
        self.assertFalse(success)

    def test_fallback_when_not_running(self):
        """
        Test that enqueuing a message is rejected when the queue is not running.

        Verifies that the queue does not accept messages unless it has been started, ensuring the event loop is not blocked and no messages are sent in this state.
        """
        # Don't start the queue
        success = self.queue.enqueue(mock_send_function, text="Immediate message")

        # Should refuse to send to prevent blocking event loop
        self.assertFalse(success)
        self.assertEqual(len(self.sent_messages), 0)

    def test_connection_state_awareness(self):
        """
        Verifies that the message queue does not send messages when the connection state indicates it should not send.

        Ensures that messages remain unsent if the queue's connection check fails, and restores the original connection check after the test.
        """

        async def async_test():
            # Mock the _should_send_message method to return False
            """
            Asynchronously tests that messages are not sent when the queue's connection state prevents sending.

            This function mocks the queue's connection check to simulate a disconnected state, enqueues a message, and verifies that the message is not sent while disconnected. The original connection check is restored after the test.
            """
            original_should_send = self.queue._should_send_message
            self.queue._should_send_message = lambda: False

            self.queue.start(message_delay=0.1)
            self.queue.ensure_processor_started()

            # Queue a message
            success = self.queue.enqueue(mock_send_function, text="Test message")
            self.assertTrue(success)

            # Wait - message should not be sent due to connection state
            await asyncio.sleep(0.3)
            self.assertEqual(len(self.sent_messages), 0)

            # Restore original method
            self.queue._should_send_message = original_should_send

        self.loop.run_until_complete(async_test())

    @pytest.mark.usefixtures("comprehensive_cleanup")
    def test_error_handling(self):
        """
        Verify that the MessageQueue survives exceptions raised by send functions and continues processing.

        Starts the queue, enqueues a message whose send function raises an exception, waits for processing, and asserts the queue remains running (i.e., the exception does not stop the processor).
        """

        async def async_test():
            """
            Verify that the message queue remains running when a send function raises an exception.

            This asynchronous test enqueues a send function that raises, starts the queue processor, waits briefly for processing, and asserts that the queue's running state is preserved (i.e., the processor did not crash).
            """

            def failing_send_function(text, **kwargs):
                raise Exception("Send failed")

            self.queue.start(message_delay=0.1)
            self.queue.ensure_processor_started()

            # Queue a message that will fail
            success = self.queue.enqueue(failing_send_function, text="Failing message")
            self.assertTrue(success)  # Queuing should succeed

            # Wait for processing - should not crash
            await asyncio.sleep(0.3)
            # Queue should continue working after error
            self.assertTrue(self.queue.is_running())

        self.loop.run_until_complete(async_test())


class TestGlobalFunctions(unittest.TestCase):
    """Test cases for global queue functions."""

    def setUp(self):
        """
        Prepares the test environment by clearing the call history of the mock send function before each test.
        """
        # Clear mock function calls for each test
        mock_send_function.calls.clear()

    def test_queue_message_function(self):
        """
        Test that the global queue_message function refuses to enqueue messages when the queue is not running.

        Verifies that queue_message returns False and does not send messages if the message queue is inactive.
        """
        # Test with queue not running (should refuse to send)
        success = queue_message(
            mock_send_function,
            text="Test message",
            description="Global function test",
        )

        # Should refuse to send when queue not running to prevent event loop blocking
        self.assertFalse(success)
        self.assertEqual(len(mock_send_function.calls), 0)


class TestQueuedMessage(unittest.TestCase):
    """Test cases for the QueuedMessage dataclass."""

    def test_message_creation(self):
        """
        Verify that a QueuedMessage instance is correctly created with the expected attributes.
        """

        def dummy_function():
            """
            A placeholder function that performs no operation.
            """
            pass

        message = QueuedMessage(
            timestamp=123.456,
            send_function=dummy_function,
            args=("arg1", "arg2"),
            kwargs={"key": "value"},
            description="Test message",
        )

        self.assertEqual(message.timestamp, 123.456)
        self.assertEqual(message.send_function, dummy_function)
        self.assertEqual(message.args, ("arg1", "arg2"))
        self.assertEqual(message.kwargs, {"key": "value"})
        self.assertEqual(message.description, "Test message")


class TestMessageQueueMethods(unittest.TestCase):
    """Test cases for additional MessageQueue methods."""

    def test_ensure_processor_started(self):
        """Test ensure_processor_started method when event loop is available."""
        queue = MessageQueue()

        # Start the queue with custom delay
        queue.start(message_delay=0.1)

        # Test ensure_processor_started method
        queue.ensure_processor_started()

        # Verify processor is running
        self.assertTrue(queue._running)

        # Clean up
        queue.stop()

    def test_stop_method(self):
        """Test stop method functionality."""
        queue = MessageQueue()

        # Start the queue
        queue.start(message_delay=0.1)
        self.assertTrue(queue._running)

        # Stop the queue
        queue.stop()
        self.assertFalse(queue._running)

        # Verify processor task is cleaned up
        self.assertIsNone(queue._processor_task)


if __name__ == "__main__":
    # Run tests
    unittest.main(verbosity=2)
