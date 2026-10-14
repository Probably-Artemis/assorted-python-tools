"""Random English words, drawn from OS entropy and thus safe for passwords."""
# make secure for shits and giggles, secrets has same syntax as random but pulls from OS entropy 
# and thus can be used for things like passwords
from random import randint
from secrets import choice

from english_words import get_english_words_set

words = tuple(
    w for w in get_english_words_set(['web2'], lower=True)
    if 4 <= len(w) <= 14
)

__all__=["randomword","randomwords"]

def randomword():
    """Return one random English word. Randomness pulls from device entropy."""
    return choice(words)

def randomwords(a, b, string=False):
    """Return a random number of random words, between a and b inclusive.

    :param a: start of the random range.
    :param b: end of the random range.
    :param string: if true, return one space-separated string; if false, return a list.
    :return: the words as a list, or as a string when string is true.
    """
    output = " ".join(randomword() for _ in range(randint(a, b)))
    if string:
        return output
    else:
        return output.split()
