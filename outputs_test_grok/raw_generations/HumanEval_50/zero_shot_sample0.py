def decode_shift(s: str) -> str:
    """
    Takes as input a lowercase string encoded as follows:
        - Shift every letter by 5 in the alphabet.

    This function should return the decoded string.
    """
    result = []
    for char in s:
        # Shift back by 5 positions in the alphabet
        # (c - 'a' - 5 + 26) % 26 + 'a'
        shifted = chr((ord(char) - ord('a') - 5 + 26) % 26 + ord('a'))
        result.append(shifted)
    return ''.join(result)