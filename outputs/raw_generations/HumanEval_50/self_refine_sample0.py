def decode_shift(s: str) -> str:
    """
    Decode a lowercase string where each letter was shifted forward by 5.
    To decode, shift each letter backward by 5 in the alphabet.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    result = []
    for ch in s:
        if not ('a' <= ch <= 'z'):
            raise ValueError("Input must contain only lowercase letters")
        # Shift backward by 5, wrapping around the alphabet
        decoded_char = chr((ord(ch) - ord('a') - 5) % 26 + ord('a'))
        result.append(decoded_char)
    return ''.join(result)