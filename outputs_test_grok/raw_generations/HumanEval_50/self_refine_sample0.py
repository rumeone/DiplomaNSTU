"""
Module providing functions for decoding strings that have been
encoded by shifting each letter by 5 positions in the alphabet.
"""


def decode_shift(s: str) -> str:
    """
    Takes as input a lowercase string encoded as follows:
        - Shift every letter by 5 in the alphabet.

    This function should return the decoded string.

    Examples:
        >>> decode_shift("cryim")
        "xmtdh"
        >>> decode_shift("zlsebmzxbqrvxkrwlqvrvgpmbrgerh")
        "ugnzwhuswlmqsfmrglqmqbkhwmbzmc"
    """
    if not s:
        return ""

    # To decode a shift of +5, we shift backwards by 5.
    # This is equivalent to shifting forward by 21 (26 - 5).
    shift = 21
    decoded = []

    for char in s:
        # Since input is guaranteed to be lowercase letters,
        # we can safely compute the new position.
        # (ord('a') = 97)
        new_pos = (ord(char) - ord('a') + shift) % 26
        decoded.append(chr(ord('a') + new_pos))

    return "".join(decoded)