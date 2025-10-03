"""
ConnectOnion Debugging Decorators

This module provides the @replay decorator for quick tool re-execution during debugging.

For xray debugging features, see connectonion.xray module.
"""

import functools
import builtins
from typing import Any, Callable


# =============================================================================
# Replay Function and Decorator
# =============================================================================

class ReplayFunction:
    """
    Container for replay functionality.

    Holds the current function and its arguments to enable re-execution
    with modified parameters during debugging.
    """

    def __init__(self):
        """Initialize with no active function."""
        self._func = None
        self._args = None
        self._kwargs = None
        self._original_func = None

    def _setup(self, func: Callable, args: tuple, kwargs: dict) -> None:
        """
        Set up replay context (internal use).

        Args:
            func: The function to replay
            args: Original positional arguments
            kwargs: Original keyword arguments
        """
        self._func = func
        self._args = args
        self._kwargs = kwargs
        self._original_func = func

    def _clear(self) -> None:
        """Clear replay context after execution (internal use)."""
        self._func = None
        self._args = None
        self._kwargs = None
        self._original_func = None

    def __call__(self, **new_kwargs) -> Any:
        """
        Replay the function with modified parameters.

        Args:
            **new_kwargs: Keyword arguments to override

        Returns:
            Result of re-executing the function

        Example:
            # In debugger at breakpoint:
            >>> replay(threshold=0.8)  # Re-run with new threshold
            🔄 Replaying my_function()
               Modified parameters: {'threshold': 0.8}
            ✅ Result: 0.95
        """
        if self._func is None:
            print("❌ No function to replay. Make sure you're in a breakpoint "
                  "inside a @replay decorated function.")
            return None

        # Merge original kwargs with new ones (new ones override)
        merged_kwargs = self._kwargs.copy() if self._kwargs else {}
        merged_kwargs.update(new_kwargs)

        print(f"🔄 Replaying {self._original_func.__name__}()")
        if new_kwargs:
            print(f"   Modified parameters: {new_kwargs}")

        try:
            result = self._func(*self._args, **merged_kwargs)
            print(f"✅ Result: {result}")
            return result
        except Exception as e:
            print(f"❌ Error during replay: {e}")
            raise

    def __repr__(self):
        """Show current replay state."""
        if self._original_func:
            return f"<replay function for {self._original_func.__name__}>"
        return "<replay function (not active)>"


class ReplayDecorator:
    """
    Hybrid object that acts as both a decorator and replay function.

    Dual-purpose design:
    1. When decorating a function, enables replay functionality
    2. When called with kwargs, replays the current function
    """

    def __init__(self, replay_func: ReplayFunction):
        """
        Initialize with a replay function container.

        Args:
            replay_func: ReplayFunction instance to manage replay state
        """
        self._replay_func = replay_func
        # Make this available globally as 'replay' for easy access
        builtins.replay = self

    def __call__(self, *args, **kwargs) -> Any:
        """
        Act as decorator or replay function based on arguments.

        If called with a single callable argument and no kwargs, acts as decorator.
        Otherwise, forwards the call to replay the current function.

        Args:
            *args: Positional arguments
            **kwargs: Keyword arguments

        Returns:
            Decorated function or replay result
        """
        # Check if being used as decorator
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            func = args[0]

            @functools.wraps(func)
            def wrapper(*inner_args, **inner_kwargs):
                # Set up replay context with current execution
                self._replay_func._setup(func, inner_args, inner_kwargs)

                try:
                    # Execute the original function
                    return func(*inner_args, **inner_kwargs)
                finally:
                    # Clean up replay context
                    self._replay_func._clear()

            # Mark function as replay-enabled
            wrapper.__replay_enabled__ = True
            return wrapper

        # Otherwise, act as the replay function
        else:
            return self._replay_func(*args, **kwargs)

    def __repr__(self):
        """Delegate representation to replay function."""
        return repr(self._replay_func)


# Create the global replay instance
replay_function = ReplayFunction()
replay = ReplayDecorator(replay_function)


# =============================================================================
# Combined Decorator
# =============================================================================

def xray_replay(func: Callable) -> Callable:
    """
    Convenience decorator that combines @xray and @replay.

    Equivalent to:
        @xray
        @replay
        def my_tool(...):
            ...

    Args:
        func: Function to decorate

    Returns:
        Function with both xray and replay capabilities
    """
    from .xray import xray
    return xray(replay(func))


# =============================================================================
# Helper Functions
# =============================================================================

def _is_replay_enabled(func: Callable) -> bool:
    """
    Check if a function has the @replay decorator.

    Args:
        func: Function to check

    Returns:
        True if function is decorated with @replay
    """
    return getattr(func, '__replay_enabled__', False)