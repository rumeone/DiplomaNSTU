def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    word_to_digit = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': -1, 'eight': 8, 'nine': 9
    }
    
    # Handle empty input
    if not numbers:
        return ''
    
    # Split and filter out empty strings
    tokens = [token for token in numbers.split() if token]
    
    # Validate tokens and sort
    try:
        sorted_tokens = sorted(tokens, key=lambda word: word_to_digit[word])
    except KeyError as e:
        raise ValueError(f"Invalid number word: {e.args[0]}") from e
    
    return ' '.join(sorted_tokens)