"""Replacement for the built-in input function with styled prompts and default responses."""
import shutil

from .ansiText import *

__all__ = ["input"]

standardinput = input # prevent unbounded recursion


def input(prompt="", styling=f"{style.UNDERLINE}", default=""):
    """Prompt the user for input, styling their typed response and optionally offering a default.

    :param prompt: the prompt shown to the user.
    :param styling: ANSI codes applied to the user's typed response. Styling is reset afterward.
    :param default: optional response shown in gray on the input line. Returned if the user enters nothing.
    :return: the user's response as a string, or default if the response was empty.
    """
    _terminal_size = shutil.get_terminal_size()
    if not default:
        prompt += styling
        response = standardinput(prompt)
    else:
        creturn = f"\n{color.BRIGHT_BLACK}{default}{style.RESET}{style.CARRIAGE_RETURN}"
        prompt += creturn
        prompt += styling
        response = standardinput(prompt)
        if response:
            extra = _terminal_size.columns - len(response)
            up = f"{cursor.COLUMN_1}{cursor.up()}"
            print(f"{up}{styling}{response}{style.RESET}{" " * extra}")
        else:
            response = default
    reset()
    return response
