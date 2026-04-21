"""
Module for decoding strings encoded with a Caesar cipher shift of 5.
"""


def decode_shift(s: str) -> str:
    """
    Decode a lowercase string encoded by shifting every letter by 5 in the alphabet.

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
        if not char.isalpha():
            decoded_chars.append(char)
            continue

        shifted_code = ord(char) - 5
        if shifted_code < ord('a'):
            shifted_code += 26

        decoded_chars.append(chr(shifted_code))

    return ''.join(decoded_chars)