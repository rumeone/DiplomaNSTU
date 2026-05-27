"""Sort a string of space-delimited English numerals from smallest to largest."""

from typing import Dict


def sort_numbers(numbers: str) -> str:
    """
    Sort a space-delimited string of English numerals from smallest to largest.

    Args:
        numbers: A string containing space-delimited English numerals from
                 'zero' to 'nine'.

    Returns:
        A string with the numerals sorted from smallest to largest,
        separated by single spaces.
    """
    word_to_digit: Dict[str, int] = {
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

    # Split the input string, filter out empty strings from extra spaces
    words = [word for word in numbers.split() if word]

    # Sort based on the numeric value from the mapping
    sorted_words = sorted(words, key=lambda w: word_to_digit[w])

    # Join back with single spaces
    return " ".join(sorted_words)