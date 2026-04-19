def decode_shift(s: str) -> str:
    """
    Takes as input a lowercase string encoded as follows:
        - Shift every letter by 5 in the alphabet.

    This function should return the decoded string.
    """
    decoded_chars = []
    for ch in s:
        # Shift the character back by 5 positions in the alphabet
        shifted_char = chr((ord(ch) - ord('a') - 5) % 26 + ord('a'))
        decoded_chars.append(shifted_char)
    return ''.join(decoded_chars)