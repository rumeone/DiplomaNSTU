"""Utility for generating space-delimited integer sequences."""

def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    If n is negative, return an empty string.
    """
    if n < 0:
        return ""
    numbers = [str(i) for i in range(n + 1)]
    return " ".join(numbers)