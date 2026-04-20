def truncate_number(number: float) -> float:
    """
    Return the decimal part of a positive floating point number.
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part