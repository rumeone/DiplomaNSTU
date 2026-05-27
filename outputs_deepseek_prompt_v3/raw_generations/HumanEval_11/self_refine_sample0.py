"""Module for performing binary XOR on strings of 1s and 0s."""


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two strings consisting only of 1s and 0s.

    Args:
        a: First binary string.
        b: Second binary string.

    Returns:
        Result of XOR operation as a string.

    Example:
        >>> string_xor('10', '110')
        '100'
    """
    max_len = max(len(a), len(b))
    padded_a = a.zfill(max_len)
    padded_b = b.zfill(max_len)

    result_chars = []
    for char_a, char_b in zip(padded_a, padded_b):
        if char_a == char_b:
            result_chars.append('0')
        else:
            result_chars.append('1')

    return ''.join(result_chars)