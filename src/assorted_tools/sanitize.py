"""Sanitize strings by removing or replacing unwanted characters.

Every mode is its own function, and can also be picked by name through sanitize.
These modes clean text for display, storage, and naming. They do not make text safe to place inside HTML, SQL, or a shell command. 
For those, use html.escape, query parameters, and shlex.quote.
"""

import re
import unicodedata

__all__ = [
    "MODES",
    "collapse_whitespace",
    "keep_alphanumeric",
    "safe_filename",
    "sanitize",
    "slugify",
    "strip_ansi",
    "strip_control",
    "strip_invisible",
    "terminal_safe",
    "to_ascii",
]

_ANSI = re.compile(r'\x1b\[[\x30-\x3f]*[\x20-\x2f]*[\x40-\x7e]|\x1b\][^\x07\x1b]*(?:\x07|\x1b\\)')

_CONTROL = re.compile(r'[\x00-\x08\x0b-\x1f\x7f-\x9f]')

_INVISIBLE = re.compile(
    r'[­؜᠎​-‏‪-‮⁠-⁤⁦-⁩﻿'  # noqa: PLE2502, PLE2515
    r'\U000e0000-\U000e007f]'
)

_NOT_ALPHANUMERIC = re.compile(r'[\W_]')
_NOT_SLUG = re.compile(r'[^a-z0-9]+')

# characters Windows forbids in file names, plus control characters and delete
_FILENAME_FORBIDDEN = re.compile(r'[<>:"/\\|?*\x00-\x1f\x7f]')

# names Windows reserves for devices, with or without an extension
_DEVICE_NAMES = {"con", "prn", "aux", "nul"} | {
    f"{port}{number}" for port in ("com", "lpt") for number in "123456789¹²³"
}


def strip_ansi(content):
    """Remove ANSI escape sequences, such as color codes, cursor movement, and window titles.

    Sequences that are cut off or malformed are left in place. Use strip_control afterward,
    or terminal_safe in place of both, to remove any escape characters left behind.

    :param content: the string to clean.
    :return: the string without escape sequences.
    """
    return _ANSI.sub('', content)


def strip_control(content):
    """Remove control characters, keeping only tab and newline.

    This removes the escape character, bell, backspace, carriage return, null, and delete,
    among others. Run strip_ansi first, or the visible remains of escape sequences, such
    as "[31m", will be left in the text.

    :param content: the string to clean.
    :return: the string without control characters.
    """
    return _CONTROL.sub('', content)


def strip_invisible(content):
    """Remove characters that take up no space on screen but change how text reads.

    This covers zero width characters, text direction marks and overrides, the soft
    hyphen, the byte order mark, and tag characters. The zero width joiner is among them,
    so emoji built by joining several emoji will fall apart into their pieces.

    :param content: the string to clean.
    :return: the string without invisible characters.
    """
    return _INVISIBLE.sub('', content)


def terminal_safe(content):
    """Make text safe to print to a terminal.

    Runs strip_ansi, strip_control, and strip_invisible, in that order.

    :param content: the string to clean.
    :return: the string with nothing left that can restyle, move, or disguise terminal output.
    """
    return strip_invisible(strip_control(strip_ansi(content)))


def collapse_whitespace(content):
    """Replace every run of whitespace with one space, and trim both ends.

    Newlines and tabs count as whitespace, so the result is always a single line.

    :param content: the string to clean.
    :return: the string on one line with single spaces between words.
    """
    return ' '.join(content.split())


def keep_alphanumeric(content):
    """Remove everything except letters and digits.

    Letters and digits from every script are kept. Spaces, punctuation, and underscores
    are removed. Run to_ascii first to keep only unaccented English letters and 0 to 9.

    :param content: the string to clean.
    :return: the string with only letters and digits.
    """
    return _NOT_ALPHANUMERIC.sub('', content)


def to_ascii(content):
    """Reduce text to plain ASCII.

    Accented letters lose their accents, so "naïve" becomes "naive". Characters with no
    ASCII form, such as "ß" or "日", are dropped.

    :param content: the string to convert.
    :return: the string with only ASCII characters.
    """
    return unicodedata.normalize('NFKD', content).encode('ascii', 'ignore').decode('ascii')


def safe_filename(content):
    """Turn text into a name that is safe to use for one file or folder on any system.

    Path separators, the other characters Windows forbids, and control characters each
    become an underscore, so the result can never point into another directory. Invisible
    characters are removed. Whitespace at both ends and periods at the end are trimmed.
    Names Windows reserves for devices, such as "CON" or "NUL.txt", get an underscore in
    front. Length is not limited.

    :param content: the proposed name. Pass a single name, not a path.
    :return: the safe name. An underscore is returned if nothing usable is left.
    """
    content = strip_invisible(content)
    content = _FILENAME_FORBIDDEN.sub('_', content)
    content = content.strip().rstrip('. ')
    if content.split('.', 1)[0].strip().lower() in _DEVICE_NAMES:
        content = '_' + content
    return content or '_'


def slugify(content):
    """Turn text into a lowercase identifier made of letters, digits, and hyphens.

    The text is reduced to ASCII and lowercased, then every run of other characters
    becomes one hyphen. "Hello, World!" becomes "hello-world".

    :param content: the string to convert.
    :return: the slug. An empty string is returned if nothing usable is left.
    """
    return _NOT_SLUG.sub('-', to_ascii(content).lower()).strip('-')


MODES = {
    "alphanumeric": keep_alphanumeric,
    "ansi": strip_ansi,
    "ascii": to_ascii,
    "control": strip_control,
    "filename": safe_filename,
    "invisible": strip_invisible,
    "slug": slugify,
    "terminal": terminal_safe,
    "whitespace": collapse_whitespace,
}


def sanitize(content, *modes):
    """Clean a string with one or more modes, applied in the order given.

    :param content: the string to clean.
    :param modes: each mode is either a name from MODES or a function that takes a string and returns a string. Names ignore case. With no modes, "alphanumeric" is used.
    :return: the cleaned string.
    :raises ValueError: if a mode is neither a known name nor a function.
    """
    if not modes:
        modes = ("alphanumeric",)
    steps = []
    for mode in modes:
        step = mode if callable(mode) else MODES.get(str(mode).lower())
        if step is None:
            raise ValueError(f"unknown mode {mode!r}, expected a function or one of: {', '.join(MODES)}")
        steps.append(step)
    for step in steps:
        content = step(content)
    return content
