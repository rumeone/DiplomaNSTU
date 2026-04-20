def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    word_to_digit = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string, strip whitespace, and filter out empty strings
    tokens = [token.strip() for token in numbers.split() if token.strip()]
    
    # Sort tokens based on their numeric values
    sorted_tokens = sorted(tokens, key=lambda word: word_to_digit[word])
    
    # Join sorted tokens with a single space
    return ' '.join(sorted_tokens)