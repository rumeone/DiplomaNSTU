def decode_shift(s: str) -> str:
    """
    Takes as input a lowercase string encoded as follows:
        - Shift every letter by 5 in the alphabet.

    This function should return the decoded string.
    """
    return "".join(
        chr((ord(c) - ord("a") - 5) % 26 + ord("a")) for c in s
    )