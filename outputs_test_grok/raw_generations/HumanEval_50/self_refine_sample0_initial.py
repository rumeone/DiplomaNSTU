"""
Module for decoding strings that have been encoded by shifting
each letter by 5 positions in the alphabet.
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

    # To decode a shift of +5, we shift backwards by 5 positions.
    # This is equivalent to shifting forward by 21 positions (26 - 5).
    shift = 21
    decoded = []

    for char in s:
        # Since input is guaranteed to be lowercase letters,
        # we can safely compute the decoded character.
        # (ord('a') = 97)
        decoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        decoded.append(decoded_char)

    return "".join(decoded)