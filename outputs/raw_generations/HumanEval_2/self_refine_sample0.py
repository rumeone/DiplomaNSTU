def truncate_number(number: float) -> float:
    """
    Return the decimal part of a positive floating point number.
    """
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    if number < 0:
        raise ValueError("Input must be positive")
    
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part