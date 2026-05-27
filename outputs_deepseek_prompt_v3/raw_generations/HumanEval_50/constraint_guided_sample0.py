"""
Module for decoding strings encoded with a Caesar cipher shift of 5.
"""


def decode_shift(s: str) -> str:
    """
    Decode a lowercase string encoded by shifting every letter by 5 positions
    forward in the alphabet.

    The function shifts each character back by 5 positions to recover the
    original string. Only lowercase letters are processed; other characters
    are left unchanged.

    Args:
        s: The encoded lowercase string.

    Returns:
        The decoded string.

    Examples:
        >>> decode_shift("cryim")
        "xmtdh"
        >>> decode_shift("zlsebmzxbqrvxkrwlqvrvgpmbrgerh")
        "ugnzwhuswlmqsfmrglqmqbkhwmbzmc"
    """
    decoded_chars = []
    for char in s:
        if 'a' <= char <= 'z':
            # Shift back by 5, wrapping around the alphabet
            decoded_char = chr((ord(char) - ord('a') - 5) % 26 + ord('a'))
            decoded_chars.append(decoded_char)
        else:
            decoded_chars.append(char)
    return ''.join(decoded_chars)