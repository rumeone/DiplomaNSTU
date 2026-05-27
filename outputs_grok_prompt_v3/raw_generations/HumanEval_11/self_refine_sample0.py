"""Binary string XOR operations."""

from typing import Tuple


def _pad_to_equal_length(a: str, b: str) -> Tuple[str, str]:
    """Return copies of a and b padded on the left with zeros to equal length."""
    max_len = max(len(a), len(b))
    return a.zfill(max_len), b.zfill(max_len)


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Example:
        >>> string_xor('10', '110')
        '100'
    """
    padded_a, padded_b = _pad_to_equal_length(a, b)
    return "".join(str(int(bit_a) ^ int(bit_b)) for bit_a, bit_b in zip(padded_a, padded_b))