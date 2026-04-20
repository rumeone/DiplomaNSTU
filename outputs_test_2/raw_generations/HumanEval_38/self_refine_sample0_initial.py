"""
Cyclic encoding and decoding functions for strings.
"""


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))]
              for i in range((len(s) + 2) // 3)]
    
    # Reverse the cyclic shift for each full group
    decoded_groups = []
    for group in groups:
        if len(group) == 3:
            # Reverse the cyclic shift: last character moves to front
            decoded_group = group[-1] + group[:-1]
            decoded_groups.append(decoded_group)
        else:
            # Groups with fewer than 3 characters remain unchanged
            decoded_groups.append(group)
    
    return "".join(decoded_groups)