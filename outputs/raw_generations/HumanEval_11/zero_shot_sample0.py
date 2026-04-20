from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Example:
        >>> string_xor('10', '110')
        '100'
    """
    # Pad the shorter string with leading zeros
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    result = []
    for bit_a, bit_b in zip(a, b):
        # XOR: 1 if bits are different, 0 if same
        if bit_a != bit_b:
            result.append('1')
        else:
            result.append('0')
    
    return ''.join(result)