"""Binary string XOR operations."""

from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Example:
        >>> string_xor('10', '110')
        '100'
    """
    max_len = max(len(a), len(b))
    a_padded = a.zfill(max_len)
    b_padded = b.zfill(max_len)
    result_bits: List[str] = []
    for bit_a, bit_b in zip(a_padded, b_padded):
        result_bits.append("1" if bit_a != bit_b else "0")
    return "".join(result_bits)