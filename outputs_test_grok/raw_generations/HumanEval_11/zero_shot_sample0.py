from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Example:
        >>> string_xor('10', '110')
        '100'
    """
    # Make both strings the same length by padding the shorter one with leading zeros
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    
    result = []
    for char_a, char_b in zip(a, b):
        # XOR the bits: '1' if different, '0' if same
        xor_bit = '1' if char_a != char_b else '0'
        result.append(xor_bit)
    
    return ''.join(result)