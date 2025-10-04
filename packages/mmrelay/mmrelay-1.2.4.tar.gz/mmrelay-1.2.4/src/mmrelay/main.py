"""
This script connects a Meshtastic mesh network to Matrix chat rooms by relaying messages between them.
It uses Meshtastic-python and Matrix nio client library to interface with the radio and the Matrix server respectively.
"""

import asyncio
import concurrent.futures
import signal
import sys

from nio import (
    MegolmEvent,
    ReactionEvent,
    RoomMessageEmote,
    RoomMessageNotice,
    RoomMessageText,
)
from nio.events.room_events import RoomMemberEvent

# Import version from package
# Import meshtastic_utils as a module to set event_loop
from mmrelay import __version__, meshtastic_utils
from mmrelay.cli_utils import msg_suggest_check_config, msg_suggest_generate_config
from mmrelay.constants.app import APP_DISPLAY_NAME, WINDOWS_PLATFORM
from mmrelay.db_utils import (
    initialize_database,
    update_longnames,
    update_shortnames,
    wipe_message_map,
)
from mmrelay.log_utils import get_logger
from mmrelay.matrix_utils import (
    connect_matrix,
    join_matrix_room,
)
from mmrelay.matrix_utils import logger as matrix_logger
from mmrelay.matrix_utils import (
    on_decryption_failure,
    on_room_member,
    on_room_message,
)
from mmrelay.meshtastic_utils import connect_meshtastic
from mmrelay.meshtastic_utils import logger as meshtastic_logger
from mmrelay.message_queue import (
    DEFAULT_MESSAGE_DELAY,
    get_message_queue,
    start_message_queue,
    stop_message_queue,
)
from mmrelay.plugin_loader import load_plugins

# Initialize logger
logger = get_logger(name=APP_DISPLAY_NAME)


# Flag to track if banner has been printed
_banner_printed = False


def print_banner():
    """
    Log the MMRelay startup banner with version information once.

    This records an informational message "Starting MMRelay version <version>" via the module logger
    the first time it is called and sets a module-level flag to prevent subsequent prints.
    """
    global _banner_printed
    # Only print the banner once
    if not _banner_printed:
        logger.info(f"Starting MMRelay version {__version__}")
        _banner_printed = True


async def main(config):
    """
    Coordinate the asynchronous relay loop between Meshtastic and Matrix clients.

    Initializes the database and plugins, starts the message queue, connects to Meshtastic and Matrix, joins configured Matrix rooms, registers event callbacks, monitors connection health, runs the Matrix sync loop with automatic retries, and ensures an orderly shutdown of all components (including optional message map wiping on startup and shutdown).

    Parameters:
        config (dict): Application configuration mapping. Expected keys used by this function include:
            - "matrix_rooms": list of room dicts with at least an "id" entry,
            - "meshtastic": optional dict with "message_delay",
            - "database" (preferred) or legacy "db": optional dict containing "msg_map" with "wipe_on_restart" boolean.

    Raises:
        ConnectionError: If connecting to Matrix fails and no Matrix client can be obtained.
    """
    # Extract Matrix configuration
    from typing import List

    matrix_rooms: List[dict] = config["matrix_rooms"]

    loop = asyncio.get_running_loop()
    meshtastic_utils.event_loop = loop

    # Initialize the SQLite database
    initialize_database()

    # Check database config for wipe_on_restart (preferred format)
    database_config = config.get("database", {})
    msg_map_config = database_config.get("msg_map", {})
    wipe_on_restart = msg_map_config.get("wipe_on_restart", False)

    # If not found in database config, check legacy db config
    if not wipe_on_restart:
        db_config = config.get("db", {})
        legacy_msg_map_config = db_config.get("msg_map", {})
        legacy_wipe_on_restart = legacy_msg_map_config.get("wipe_on_restart", False)

        if legacy_wipe_on_restart:
            wipe_on_restart = legacy_wipe_on_restart
            logger.warning(
                "Using 'db.msg_map' configuration (legacy). 'database.msg_map' is now the preferred format and 'db.msg_map' will be deprecated in a future version."
            )

    if wipe_on_restart:
        logger.debug("wipe_on_restart enabled. Wiping message_map now (startup).")
        wipe_message_map()

    # Load plugins early
    load_plugins(passed_config=config)

    # Start message queue with configured message delay
    message_delay = config.get("meshtastic", {}).get(
        "message_delay", DEFAULT_MESSAGE_DELAY
    )
    start_message_queue(message_delay=message_delay)

    # Connect to Meshtastic
    meshtastic_utils.meshtastic_client = await asyncio.to_thread(
        connect_meshtastic, passed_config=config
    )

    # Connect to Matrix
    matrix_client = await connect_matrix(passed_config=config)

    # Check if Matrix connection was successful
    if matrix_client is None:
        # The error is logged by connect_matrix, so we can just raise here.
        raise ConnectionError(
            "Failed to connect to Matrix. Cannot continue without Matrix client."
        )

    # Join the rooms specified in the config.yaml
    for room in matrix_rooms:
        await join_matrix_room(matrix_client, room["id"])

    # Register the message callback for Matrix
    matrix_logger.info("Listening for inbound Matrix messages...")
    matrix_client.add_event_callback(
        on_room_message,
        (RoomMessageText, RoomMessageNotice, RoomMessageEmote, ReactionEvent),
    )
    # Add E2EE callbacks - MegolmEvent only goes to decryption failure handler
    # Successfully decrypted messages will be converted to RoomMessageText etc. by matrix-nio
    matrix_client.add_event_callback(on_decryption_failure, (MegolmEvent,))
    # Add RoomMemberEvent callback to track room-specific display name changes
    matrix_client.add_event_callback(on_room_member, (RoomMemberEvent,))

    # Set up shutdown event
    shutdown_event = asyncio.Event()

    async def shutdown():
        """
        Signal the application to begin shutdown.

        Set the Meshtastic shutdown flag and set the local shutdown event so any coroutines waiting on that event can start cleanup.
        """
        matrix_logger.info("Shutdown signal received. Closing down...")
        meshtastic_utils.shutting_down = True  # Set the shutting_down flag
        shutdown_event.set()

    # Handle signals differently based on the platform
    if sys.platform != WINDOWS_PLATFORM:
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, lambda: asyncio.create_task(shutdown()))
    else:
        # On Windows, we can't use add_signal_handler, so we'll handle KeyboardInterrupt
        pass

    # Start connection health monitoring using getMetadata() heartbeat
    # This provides proactive connection detection for all interface types
    _ = asyncio.create_task(meshtastic_utils.check_connection())

    # Ensure message queue processor is started now that event loop is running
    get_message_queue().ensure_processor_started()

    # Start the Matrix client sync loop
    try:
        while not shutdown_event.is_set():
            try:
                if meshtastic_utils.meshtastic_client:
                    nodes_snapshot = dict(meshtastic_utils.meshtastic_client.nodes)
                    await loop.run_in_executor(
                        None,
                        update_longnames,
                        nodes_snapshot,
                    )
                    await loop.run_in_executor(
                        None,
                        update_shortnames,
                        nodes_snapshot,
                    )
                else:
                    meshtastic_logger.warning("Meshtastic client is not connected.")

                matrix_logger.info("Starting Matrix sync loop...")
                sync_task = asyncio.create_task(
                    matrix_client.sync_forever(timeout=30000)
                )

                shutdown_task = asyncio.create_task(shutdown_event.wait())

                # Wait for either the matrix sync to fail, or for a shutdown
                done, pending = await asyncio.wait(
                    [sync_task, shutdown_task],
                    return_when=asyncio.FIRST_COMPLETED,
                )

                # Cancel any pending tasks
                for task in pending:
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        pass

                if shutdown_event.is_set():
                    matrix_logger.info("Shutdown event detected. Stopping sync loop...")
                    break

                # Check if sync_task completed with an exception
                if sync_task in done:
                    try:
                        # This will raise the exception if the task failed
                        sync_task.result()
                        # If we get here, sync completed normally (shouldn't happen with sync_forever)
                        matrix_logger.warning(
                            "Matrix sync_forever completed unexpectedly"
                        )
                    except Exception:  # noqa: BLE001 — sync loop must keep retrying
                        # Log the exception and continue to retry
                        matrix_logger.exception("Matrix sync failed")
                        # The outer try/catch will handle the retry logic

            except Exception:  # noqa: BLE001 — keep loop alive for retries
                if shutdown_event.is_set():
                    break
                matrix_logger.exception("Error syncing with Matrix server")
                await asyncio.sleep(5)  # Wait briefly before retrying
    except KeyboardInterrupt:
        await shutdown()
    finally:
        # Cleanup
        matrix_logger.info("Stopping message queue...")
        stop_message_queue()

        matrix_logger.info("Closing Matrix client...")
        await matrix_client.close()
        if meshtastic_utils.meshtastic_client:
            meshtastic_logger.info("Closing Meshtastic client...")
            try:
                # Timeout wrapper to prevent infinite hanging during shutdown
                # The meshtastic library can sometimes hang indefinitely during close()
                # operations, especially with BLE connections. This timeout ensures
                # the application can shut down gracefully within 10 seconds.

                def _close_meshtastic():
                    """
                    Closes the Meshtastic client connection synchronously.
                    """
                    meshtastic_utils.meshtastic_client.close()

                with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                    future = executor.submit(_close_meshtastic)
                    future.result(timeout=10.0)  # 10-second timeout

                meshtastic_logger.info("Meshtastic client closed successfully")
            except concurrent.futures.TimeoutError:
                meshtastic_logger.warning(
                    "Meshtastic client close timed out - forcing shutdown"
                )
            except Exception as e:
                meshtastic_logger.error(
                    f"Unexpected error during Meshtastic client close: {e}",
                    exc_info=True,
                )

        # Attempt to wipe message_map on shutdown if enabled
        if wipe_on_restart:
            logger.debug("wipe_on_restart enabled. Wiping message_map now (shutdown).")
            wipe_message_map()

        # Cancel the reconnect task if it exists
        if meshtastic_utils.reconnect_task:
            meshtastic_utils.reconnect_task.cancel()
            meshtastic_logger.info("Cancelled Meshtastic reconnect task.")

        # Cancel any remaining tasks (including the check_conn_task)
        current_task = asyncio.current_task()
        pending_tasks = [
            task
            for task in asyncio.all_tasks(loop)
            if task is not current_task and not task.done()
        ]

        for task in pending_tasks:
            task.cancel()

        if pending_tasks:
            await asyncio.gather(*pending_tasks, return_exceptions=True)

        matrix_logger.info("Shutdown complete.")


def run_main(args):
    """
    Start the application: load configuration, validate required keys, and run the main async runner.

    Loads and applies configuration (optionally overriding logging level from args), initializes module configuration, verifies required configuration sections (required keys are ["meshtastic", "matrix_rooms"] when credentials.json is present, otherwise ["matrix", "meshtastic", "matrix_rooms"]), and executes the main async entrypoint. Returns process exit codes: 0 for successful completion or user interrupt, 1 for configuration errors or unhandled exceptions.

    Parameters:
        args: Parsed command-line arguments (may be None). Recognized option used here: `log_level` to override the configured logging level.

    Returns:
        int: Exit code (0 on success or user-initiated interrupt, 1 on failure such as invalid config or runtime error).
    """
    # Print the banner at startup
    print_banner()

    # Load configuration
    from mmrelay.config import load_config

    # Load configuration with args
    config = load_config(args=args)

    # Handle the --log-level option
    if args and args.log_level:
        # Override the log level from config
        if "logging" not in config:
            config["logging"] = {}
        config["logging"]["level"] = args.log_level

    # Set the global config variables in each module
    from mmrelay import (
        db_utils,
        log_utils,
        matrix_utils,
        meshtastic_utils,
        plugin_loader,
    )
    from mmrelay.config import set_config
    from mmrelay.plugins import base_plugin

    # Use the centralized set_config function to set up the configuration for all modules
    set_config(matrix_utils, config)
    set_config(meshtastic_utils, config)
    set_config(plugin_loader, config)
    set_config(log_utils, config)
    set_config(db_utils, config)
    set_config(base_plugin, config)

    # Configure component debug logging now that config is available
    log_utils.configure_component_debug_logging()

    # Get config path and log file path for logging
    from mmrelay.config import config_path
    from mmrelay.log_utils import log_file_path

    # Create a logger with a different name to avoid conflicts with the one in config.py
    config_rich_logger = get_logger("ConfigInfo")

    # Now log the config file and log file locations with the properly formatted logger
    if config_path:
        config_rich_logger.info(f"Config file location: {config_path}")
    if log_file_path:
        config_rich_logger.info(f"Log file location: {log_file_path}")

    # Check if config exists and has the required keys
    # Note: matrix section is optional if credentials.json exists
    from mmrelay.config import load_credentials

    credentials = load_credentials()

    if credentials:
        # With credentials.json, only meshtastic and matrix_rooms are required
        required_keys = ["meshtastic", "matrix_rooms"]
    else:
        # Without credentials.json, all sections are required
        required_keys = ["matrix", "meshtastic", "matrix_rooms"]

    # Check each key individually for better debugging
    for key in required_keys:
        if key not in config:
            logger.error(f"Required key '{key}' is missing from config")

    if not config or not all(key in config for key in required_keys):
        # Exit with error if no config exists
        missing_keys = [key for key in required_keys if key not in config]
        if credentials:
            logger.error(f"Configuration is missing required keys: {missing_keys}")
            logger.error("Matrix authentication will use credentials.json")
            logger.error("Next steps:")
            logger.error(
                f"  • Create a valid config.yaml file or {msg_suggest_generate_config()}"
            )
            logger.error(f"  • {msg_suggest_check_config()}")
        else:
            logger.error(f"Configuration is missing required keys: {missing_keys}")
            logger.error("Next steps:")
            logger.error(
                f"  • Create a valid config.yaml file or {msg_suggest_generate_config()}"
            )
            logger.error(f"  • {msg_suggest_check_config()}")
        return 1

    try:
        asyncio.run(main(config))
        return 0
    except KeyboardInterrupt:
        logger.info("Interrupted by user. Exiting.")
        return 0
    except Exception:  # noqa: BLE001 — top-level guard to log and exit cleanly
        logger.exception("Error running main functionality")
        return 1


if __name__ == "__main__":
    import sys

    from mmrelay.cli import main

    sys.exit(main())
