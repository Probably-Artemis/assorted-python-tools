# noqa: N999
"""Classes for styling and coloring text using ANSI escape characters.

:var cursor: cursor movement and screen clearing.
:var style: terminal formatting and styling.
:var color: text and background coloring.
"""

import os
import sys

__all__ = ["color", "color_allowed", "cursor", "reset", "style"]


class cursor:
    """ANSI codes to move the cursor and clear the screen."""

    COLUMN_1 = '\033[1G' # replicates \r
    HOME = '\033[H'
    HIDE = '\033[?25l'
    SHOW = '\033[?25h'
    SAVE = '\0337'
    RESTORE = '\0338'
    CLEAR_LINE = '\033[2K'
    CLEAR_TO_END = '\033[0K'
    CLEAR_SCREEN = '\033[2J'

    @staticmethod
    def up(n=1):
        """Move the cursor up n lines."""
        return f'\033[{n}A'

    @staticmethod
    def down(n=1):
        """Move the cursor down n lines."""
        return f'\033[{n}B'

    @staticmethod
    def right(n=1):
        """Move the cursor right n columns."""
        return f'\033[{n}C'

    @staticmethod
    def left(n=1):
        """Move the cursor left n columns."""
        return f'\033[{n}D'


class style:
    """ANSI codes to style and format text."""

    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    RAPID_BLINK = '\033[6m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKETHROUGH = '\033[9m'
    DOUBLE_UNDERLINE = '\033[21m' # some terminals read 21 as "bold off" instead
    CARRIAGE_RETURN = cursor.COLUMN_1 # kept for backwards compat, use cursor.COLUMN_1
#Resets:
    NORMAL_INTENSITY = '\033[22m' # undoes BOLD and DIM
    NO_ITALIC = '\033[23m'
    NO_UNDERLINE = '\033[24m' # also undoes DOUBLE_UNDERLINE
    NO_BLINK = '\033[25m'
    NO_REVERSE = '\033[27m'
    REVEAL = '\033[28m' # undoes HIDDEN
    NO_STRIKETHROUGH = '\033[29m'


class color:
    """ANSI codes to color text and background."""

#ForegroundColor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    DEFAULT = '\033[39m'
#BackgroundColor:
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    BG_BRIGHT_BLACK = '\033[100m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'
    BG_BRIGHT_BLUE = '\033[104m'
    BG_BRIGHT_MAGENTA = '\033[105m'
    BG_BRIGHT_CYAN = '\033[106m'
    BG_BRIGHT_WHITE = '\033[107m'
    BG_DEFAULT = '\033[49m'


def reset():
    """Resets text, for when previous string must leave formatting open."""
    print(style.RESET, end="")


def color_allowed(stream=sys.stdout):
    """Return True if color output is appropriate for stream.

    False when NO_COLOR is set to a non-empty value (https://no-color.org) or when stream is not a terminal, such as a pipe or file.
    """
    if os.environ.get("NO_COLOR"):
        return False
    return hasattr(stream, "isatty") and stream.isatty()
