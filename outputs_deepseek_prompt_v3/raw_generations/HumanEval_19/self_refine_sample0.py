"""
Module for sorting space-delimited textual representations of numbers.
"""

from typing import Dict


def sort_numbers(numbers: str) -> str:
    """
    Sort space-delimited textual numbers from smallest to largest.

    Args:
        numbers: A string containing space-delimited textual representations
                 of numbers from 'zero' to 'nine'.

    Returns:
        A string with the same numbers sorted from smallest to largest,
        separated by single spaces.

    Raises:
        ValueError: If any word in the input is not a valid number representation.
    """
    word_to_digit: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    if not numbers:
        return ''

    words = numbers.strip().split()
    if not words:
        return ''

    try:
        sorted_words = sorted(words, key=lambda w: word_to_digit[w])
    except KeyError as e:
        raise ValueError(f"Invalid number representation: {e.args[0]}") from e

    return ' '.join(sorted_words)