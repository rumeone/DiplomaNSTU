"""
Module providing cyclic encoding and decoding functions for strings.

The encode_cyclic function splits the input string into groups of three
characters and rotates each group left by one position. The decode_cyclic
function reverses this transformation.
"""


def encode_cyclic(s: str) -> str:
    """
    Returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))]
              for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group)
              == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    if not s:
        return ""

    # Process in groups of 3 characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))]
              for i in range((len(s) + 2) // 3)]

    decoded_groups = []
    for group in groups:
        if len(group) == 3:
            # To reverse the left rotation (abc -> bca), we perform a right rotation
            # which is equivalent to moving the last character to the front
            decoded_groups.append(group[-1] + group[:-1])
        else:
            # Groups with fewer than 3 characters are not rotated
            decoded_groups.append(group)

    return "".join(decoded_groups)