"""Binary XOR operation on two binary strings.

This module provides a function to perform bitwise XOR on two strings
consisting of '0's and '1's, returning the result as a binary string.
"""


from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Example:
        >>> string_xor('10', '110')
        '100'
    """
    # Ensure strings are of equal length by padding the shorter one with leading zeros
    if len(a) < len(b):
        a = a.zfill(len(b))
    elif len(b) < len(a):
        b = b.zfill(len(a))

    result: List[str] = []
    for char_a, char_b in zip(a, b):
        # XOR the bits: '1' if bits are different, '0' if they are the same
        xor_bit = '1' if char_a != char_b else '0'
        result.append(xor_bit)

    return ''.join(result)