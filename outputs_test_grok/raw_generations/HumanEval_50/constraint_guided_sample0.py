"""
Module providing functions for decoding strings encoded with a Caesar shift.
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
    # Since the encoding shifts forward by 5, decoding requires shifting backward by 5.
    # Using modulo 26 to wrap around the alphabet.
    decoded_chars = []
    for char in s:
        # Convert to 0-25 range, subtract 5, modulo 26, then back to character
        shifted = (ord(char) - ord('a') - 5) % 26
        decoded_chars.append(chr(ord('a') + shifted))
    return ''.join(decoded_chars)