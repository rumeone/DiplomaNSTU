"""Number word sorting utilities."""

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Example:
        >>> sort_numbers('three one  five ')
        'one three five'
    """
    num_map = {w: i for i, w in enumerate(
        ['zero', 'one', 'two', 'three', 'four',
         'five', 'six', 'seven', 'eight', 'nine'])}
    words = numbers.split()
    return ' '.join(sorted(words, key=num_map.get))