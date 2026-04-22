"""
Module providing decoding functionality for strings encoded by shifting
letters in the alphabet.
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
    decoded = []
    for char in s:
        # Shift back by 5 positions in the alphabet (mod 26)
        # 'a' = 0, 'b' = 1, ..., 'z' = 25
        shifted = (ord(char) - ord('a') - 5) % 26
        decoded.append(chr(ord('a') + shifted))
    return ''.join(decoded)