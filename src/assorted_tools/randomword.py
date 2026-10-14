"""Random English words, drawn from OS entropy and thus safe for passwords."""
# make secure for shits and giggles, secrets has same syntax as random but pulls from OS entropy
# and thus can be used for things like passwords
import gzip
import json
from functools import cache
from importlib import resources
from random import randint
from secrets import choice

from english_words import get_english_words_set

words = tuple(
    w for w in get_english_words_set(['web2'], lower=True)
    if 4 <= len(w) <= 14
)

# built by scripts/build_wordlists.py from Open English WordNet and the 1990 US Census name lists
KINDS = ("adjective", "adverb", "name", "noun", "proper", "surname", "verb")

__all__=["KINDS","randomword","randomwords"]

@cache
def _kind_words():
    # only loaded the first time a kind is asked for
    raw = resources.files(__package__).joinpath("data", "words.json.gz").read_bytes()
    return {kind: tuple(ws) for kind, ws in json.loads(gzip.decompress(raw)).items()}

def randomword(kind=None):
    """Return one random English word. Randomness pulls from device entropy.

    :param kind: optional word type, one of KINDS. Ignores case. With no kind, any word can come up.
    :return: the word. Names, surnames, and proper nouns are capitalized; everything else is lowercase.
    :raises ValueError: if kind is not in KINDS.
    """
    if kind is None:
        return choice(words)
    kind = str(kind).lower()
    if kind not in KINDS:
        raise ValueError(f"unknown kind {kind!r}, expected one of: {', '.join(KINDS)}")
    return choice(_kind_words()[kind])

def randomwords(a, b, string=False, kind=None):
    """Return a random number of random words, between a and b inclusive.

    :param a: start of the random range.
    :param b: end of the random range.
    :param string: if true, return one space-separated string; if false, return a list.
    :param kind: optional word type, one of KINDS, passed on to randomword.
    :return: the words as a list, or as a string when string is true.
    :raises ValueError: if kind is not in KINDS.
    """
    output = [randomword(kind) for _ in range(randint(a, b))]
    if string:
        return " ".join(output)
    else:
        return output
