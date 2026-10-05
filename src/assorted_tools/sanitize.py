"""Sanitize a string according to various frameworks, or provide your own."""

import re

__all__ = ["sanitize"]

def sanitize(content, mode=""):
    mode=mode.lower()
    if not mode or mode == "alphanumeric":
        content = re.sub(pattern=r'\W', repl='', string=content)
    return content
