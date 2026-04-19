def decode_shift(s: str) -> str:
    """
    Decode a lowercase string where each letter was shifted forward by 5.
    To decode, shift each letter backward by 5 in the alphabet.
    """
    result = []
    for ch in s:
        # Shift backward by 5, wrapping around the alphabet
        decoded_char = chr((ord(ch) - ord('a') - 5) % 26 + ord('a'))
        result.append(decoded_char)
    return ''.join(result)