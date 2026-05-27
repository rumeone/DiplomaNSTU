"""Generate space-delimited numeric sequences."""

def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    If n is negative, return an empty string.

    Examples:
        >>> string_sequence(0)
        '0'
        >>> string_sequence(5)
        '0 1 2 3 4 5'
    """
    if n < 0:
        return ""
    number_strings = [str(i) for i in range(n + 1)]
    return " ".join(number_strings)