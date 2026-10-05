"""Utilities to make toggling debug print statements easier."""

__all__ = ["set_debug", "deprint"]

debug = False


def set_debug(state=True):
    """Set whether debug print statements should execute.

    :param state: true to enable debug printing, false to disable it.
    """
    global debug
    debug = state

def get_debug():
    """Query debug state.

    :returns: debug state boolean
    """
    global debug
    return debug

def deprint(*args, **kwargs):
    """Debug print statement that behaves exactly like a standard print statement.

    Output is only produced after debugging is enabled with set_debug.
    """
    if debug:
        print(*args, **kwargs)
