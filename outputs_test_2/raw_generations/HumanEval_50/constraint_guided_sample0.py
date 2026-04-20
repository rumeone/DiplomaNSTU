"""
String decoding module for shift cipher with a fixed shift of 5.
"""


def decode_shift(s: str) -> str:
    """
    Decode a lowercase string encoded by shifting every letter by 5 positions
    forward in the alphabet (wrapping around from 'z' to 'a').

    Args:
        s: The encoded lowercase string.

    Returns:
        The decoded lowercase string.

    Examples:
        >>> decode_shift("cryim")
        'xmtdh'
        >>> decode_shift("zlsebmzxbqrvxkrwlqvrvgpmbrgerh")
        'ugnzwhuswlmqsfmrglqmqbkhwmbzmc'
    """
    decoded_chars = []
    for char in s:
        # Shift the character back by 5 positions
        decoded_char = chr((ord(char) - ord('a') - 5) % 26 + ord('a'))
        decoded_chars.append(decoded_char)
    return ''.join(decoded_chars)