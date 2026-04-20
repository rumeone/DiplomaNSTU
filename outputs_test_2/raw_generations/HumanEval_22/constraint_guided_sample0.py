from typing import List


def filter_integers(values: List[str]) -> List[int]:
    """
    Filter given list of string values only for integers.

    Example:
        >>> filter_integers(['10', ' 123 ', '5.0', 'three', 'abc', '{}'])
        [10, 123]
    """
    result = []
    
    for value in values:
        stripped_value = value.strip()
        
        # Check if string consists only of digits (with optional leading sign)
        if (stripped_value and 
            (stripped_value.isdigit() or 
             (stripped_value[0] in '+-' and stripped_value[1:].isdigit()))):
            result.append(int(stripped_value))
    
    return result