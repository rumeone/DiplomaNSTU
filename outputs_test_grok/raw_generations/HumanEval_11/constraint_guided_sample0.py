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
    # Ensure both strings are of equal length by padding the shorter one
    # with leading zeros. This maintains the binary alignment for XOR.
    max_len = max(len(a), len(b))
    a_padded = a.zfill(max_len)
    b_padded = b.zfill(max_len)

    result: List[str] = []
    for char_a, char_b in zip(a_padded, b_padded):
        # Convert characters to integers, perform XOR, and convert back to string
        xor_bit = int(char_a) ^ int(char_b)
        result.append(str(xor_bit))

    return "".join(result)