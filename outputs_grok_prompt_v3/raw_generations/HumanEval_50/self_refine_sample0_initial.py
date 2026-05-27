"""Utility for decoding alphabet-shifted strings."""

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
    decoded_chars = []
    for char in s:
        shifted = (ord(char) - ord("a") - 5) % 26 + ord("a")
        decoded_chars.append(chr(shifted))
    return "".join(decoded_chars)