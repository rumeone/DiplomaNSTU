def decode_shift(s: str) -> str:
    """
    Decode a string where each lowercase letter was shifted forward by 5 positions.
    To decode, shift each letter backward by 5 positions in the alphabet.
    """
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            # Shift backward by 5, wrapping around the alphabet
            decoded_char = chr((ord(ch) - ord('a') - 5) % 26 + ord('a'))
            result.append(decoded_char)
        else:
            # Non-lowercase letters are kept unchanged (though specification says lowercase input)
            result.append(ch)
    return ''.join(result)