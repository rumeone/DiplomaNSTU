def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Example:
        >>> sort_numbers('three one  five ')
        'one three five'
    """
    word_to_num = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    # Split on whitespace, filter out empty strings, convert to numbers, sort, convert back
    num_words = [word for word in numbers.split() if word]
    sorted_words = sorted(num_words, key=lambda w: word_to_num[w])
    return ' '.join(sorted_words)