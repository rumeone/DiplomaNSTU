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
    
    result_chars = []
    for char_a, char_b in zip(a_padded, b_padded):
        if char_a == char_b:
            result_chars.append('0')
        else:
            result_chars.append('1')
    
    result = ''.join(result_chars).lstrip('0')
    return result if result else '0'