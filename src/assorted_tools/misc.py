"""Small functions which did not warrant their own file."""
import os
import shutil
from time import sleep

from .ansiText import *
from .centerprint import *

__all__ = ["clear", "newsection", "slowprint"]

def clear(delay=0):
    """Clear the terminal.

    :param delay: optional delay in seconds to wait before clearing.
    """
    sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')

def slowprint(string, delay=0.025):
    """Print a string character by character.

    :param string: the string to print.
    :param delay: the delay in seconds between each character. Spaces use a quarter of this delay.
    """
    for char in string:
        print(char,end="",flush=True)
        if char != " ":
            sleep(delay)
        else:
            sleep(delay/4)
    print()

def newsection(character="=", delay=0.5, nl=1, title=""):
    """Print a bar across the terminal to mark a new section.

    :param character: the character to draw the bar with. Only the first character is used.
    :param delay: delay in seconds to wait before printing.
    :param nl: number of blank lines to print before the rule.
    :param title: optional argument which will use centerprint() to put the title in the center of the bar.
    """
    _terminal_size = shutil.get_terminal_size()
    sleep(delay)
    if title == "":
        print(f"{style.RESET}{color.BRIGHT_BLACK}{"\n" * nl}{character[0] * _terminal_size.columns}\n{style.RESET}")
    else:
        title = f"{style.RESET}{title}{color.BRIGHT_BLACK}"
        print(f"{style.RESET}{color.BRIGHT_BLACK}{"\n" * nl}{centerprint(title, whitespace=character, ret=True)}\n{style.RESET}")

