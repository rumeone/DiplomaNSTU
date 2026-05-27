def decode_shift(s: str) -> str:
    """
    Takes as input a lowercase string encoded as follows:
        - Shift every letter by 5 in the alphabet.

    This function should return the decoded string.

    Examples:
        >>> decode_shift("cryim")
        "xmtdh"
        >>> decode_shift("zlsebmzxbqrvxkrwlqvrvgpmbrgerh")
        "ugnzwhuswlmqsfmrglqmqbkhwmbzmc"
    """
    result = []
    for ch in s:
        if 'a' <= ch <= 'z':
            # Shift back by 5 positions
            shifted = chr((ord(ch) - ord('a') - 5) % 26 + ord('a'))
            result.append(shifted)
        else:
            # If character is not lowercase letter, keep it unchanged
            result.append(ch)
    return ''.join(result)