from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.

    Example:
        >>> string_xor('10', '110')
        '100'
    """
    if not (a.isdigit() and b.isdigit()):
        raise ValueError("Input strings must contain only digits")
    
    max_len = max(len(a), len(b))
    a_padded = a.zfill(max_len)
    b_padded = b.zfill(max_len)
    
    result_chars = []
    for char_a, char_b in zip(a_padded, b_padded):
        if char_a not in '01' or char_b not in '01':
            raise ValueError("Input strings must consist only of '0' and '1'")
        if char_a == char_b:
            result_chars.append('0')
        else:
            result_chars.append('1')
    
    result = ''.join(result_chars)
    return result.lstrip('0') or '0'