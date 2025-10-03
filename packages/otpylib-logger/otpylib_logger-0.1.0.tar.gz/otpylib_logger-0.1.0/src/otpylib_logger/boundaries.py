#!/usr/bin/env python3
"""
Logger Manager GenServer

The core GenServer that manages log routing and handler coordination.
"""

import types
from typing import Any

from otpylib import gen_server, process

from otpylib_logger.data import LoggerSpec
from otpylib_logger import core


# =============================================================================
# GenServer Callbacks
# =============================================================================

callbacks = types.SimpleNamespace()


async def init(logger_spec: LoggerSpec):
    """Initialize the logger manager."""
    print(f"[logger_manager] Starting with {len(logger_spec.handlers)} handlers")
    
    state = {
        "level": logger_spec.level,
        "handlers": [],  # Will be populated with handler PIDs
    }
    
    return state


async def handle_info(message, state):
    """Handle log messages and route to handlers."""
    print(f"[logger_manager] Received message: {message}")
    print(f"[logger_manager] Current handlers: {state['handlers']}")
    
    match message:
        case ("log", level, msg, metadata):
            print(f"[logger_manager] Processing log: level={level}, msg={msg}")
            
            # Check if we should log at this level
            if not core.should_log(level, state["level"].value):
                print(f"[logger_manager] Skipping log (below threshold)")
                return (gen_server.NoReply(), state)
            
            # Format the log entry
            entry = core.format_log_entry(level, msg, metadata)
            print(f"[logger_manager] Formatted entry: {entry}")
            
            # Route to all handlers
            print(f"[logger_manager] Routing to {len(state['handlers'])} handlers")
            for handler_pid in state["handlers"]:
                print(f"[logger_manager] Sending to handler {handler_pid}")
                await process.send(handler_pid, ("write", entry))
            
            return (gen_server.NoReply(), state)
        
        case ("add_handler", handler_pid):
            # Dynamically add a handler
            state["handlers"].append(handler_pid)
            print(f"[logger_manager] Added handler {handler_pid}")
            return (gen_server.NoReply(), state)
        
        case ("set_level", new_level):
            # Change log level at runtime
            state["level"] = new_level
            print(f"[logger_manager] Log level changed to {new_level}")
            return (gen_server.NoReply(), state)
        
        case _:
            print(f"[logger_manager] Unhandled message type")
            return (gen_server.NoReply(), state)


async def terminate(reason, state):
    """Cleanup on termination."""
    if reason is not None:
        print(f"Logger Manager terminated with error: {reason}")
    else:
        print("Logger Manager terminated normally")
    
    print(f"Final state: {len(state['handlers'])} handlers")


callbacks.init = init
callbacks.handle_info = handle_info
callbacks.terminate = terminate