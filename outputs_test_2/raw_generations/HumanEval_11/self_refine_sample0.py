from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two strings consisting only of 1s and 0s.

    Args:
        a: First binary string.
        b: Second binary string.

    Returns:
        The result of XOR operation as a binary string.

    Example:
        >>> string_xor('10', '110')
        '100'
    """
    if not a or not b:
        return a or b or ''

    max_length = max(len(a), len(b))
    padded_a = a.zfill(max_length)
    padded_b = b.zfill(max_length)

    result_chars = []
    for char_a, char_b in zip(padded_a, padded_b):
        if char_a == char_b:
            result_chars.append('0')
        else:
            result_chars.append('1')

    result = ''.join(result_chars)
    return result.lstrip('0') or '0'