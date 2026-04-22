"""
Module providing a function to sort number words in a string.
"""


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.

    Example:
        >>> sort_numbers('three one  five ')
        'one three five'
    """
    if not numbers or not numbers.strip():
        return ""

    number_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    # Split on whitespace and filter out empty strings from multiple spaces
    words = [word for word in numbers.split() if word]

    # Sort by their numeric value
    sorted_words = sorted(words, key=lambda w: number_map.get(w.lower(), float("inf")))

    return " ".join(sorted_words)