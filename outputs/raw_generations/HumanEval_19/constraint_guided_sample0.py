def sort_numbers(numbers: str) -> str:
    word_to_num = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    num_to_word = {v: k for k, v in word_to_num.items()}
    
    # Split on whitespace, filter out empty strings, and convert to numbers
    num_list = [word_to_num[word] for word in numbers.split() if word]
    
    # Sort numbers and convert back to words
    sorted_words = [num_to_word[num] for num in sorted(num_list)]
    
    return ' '.join(sorted_words)