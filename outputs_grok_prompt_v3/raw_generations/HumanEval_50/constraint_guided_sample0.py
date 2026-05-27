"""Decode strings that have been shifted forward by 5 letters."""

def decode_shift(s: str) -> str:
    """
    Takes as input a lowercase string encoded as follows:
        - Shift every letter by 5 in the alphabet.

    This function should return the decoded string.
    """
    decoded_chars = []
    for char in s:
        position = ord(char) - ord("a")
        new_position = (position - 5) % 26
        decoded_chars.append(chr(new_position + ord("a")))
    return "".join(decoded_chars)