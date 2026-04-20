"""Module for performing binary XOR operations on strings of 1s and 0s."""

from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two strings consisting only of 1s and 0s.

    Args:
        a: First binary string.
        b: Second binary string.

    Returns:
        The result of binary XOR as a string.

    Example:
        >>> string_xor('10', '110')
        '100'
    """
    max_len = max(len(a), len(b))
    a_padded = a.zfill(max_len)
    b_padded = b.zfill(max_len)

    result_chars = []
    for char_a, char_b in zip(a_padded, b_padded):
        if char_a == char_b:
            result_chars.append('0')
        else:
            result_chars.append('1')

    result = ''.join(result_chars)
    return result.lstrip('0') or '0'