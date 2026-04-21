"""
Cyclic string encoding and decoding functions.

This module provides functions to encode and decode strings by cycling
groups of three characters. The encoding rotates characters within each
3-character group, and decoding reverses this rotation.
"""


def decode_cyclic(s: str) -> str:
    """
    Decode a string encoded with the encode_cyclic function.

    Args:
        s: String that was encoded using encode_cyclic.

    Returns:
        The decoded string.

    Example:
        >>> decode_cyclic(encode_cyclic("abcdef"))
        'abcdef'
    """
    # Split the string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))]
              for i in range((len(s) + 2) // 3)]

    # Reverse the cycling operation for each group
    decoded_groups = []
    for group in groups:
        if len(group) == 3:
            # Move last character to the front to reverse the encoding
            decoded_groups.append(group[-1] + group[:-1])
        else:
            # Groups with fewer than 3 characters remain unchanged
            decoded_groups.append(group)

    return "".join(decoded_groups)