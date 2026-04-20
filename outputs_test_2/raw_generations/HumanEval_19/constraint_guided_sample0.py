"""
Module for sorting space-delimited number words from 'zero' to 'nine'.
"""


def sort_numbers(numbers: str) -> str:
    """
    Sort space-delimited number words from smallest to largest.

    Args:
        numbers: A string containing space-delimited number words
                 from 'zero' to 'nine'.

    Returns:
        A string with the number words sorted from smallest to largest,
        separated by single spaces.

    Example:
        >>> sort_numbers('three one  five ')
        'one three five'
    """
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string, filter out empty strings from extra spaces
    words = [word for word in numbers.split() if word]

    # Sort by the numeric value from the mapping
    sorted_words = sorted(words, key=lambda word: number_map[word])

    # Join back with single spaces
    return ' '.join(sorted_words)