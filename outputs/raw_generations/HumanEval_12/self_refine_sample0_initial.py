def longest(strings: List[str]) -> str:
    if not strings:
        return ""
    
    longest_string = strings[0]
    max_length = len(longest_string)
    
    for s in strings[1:]:
        current_length = len(s)
        if current_length > max_length:
            max_length = current_length
            longest_string = s
    
    return longest_string