def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, return the decimal part.
    """
    integer_part = int(number)
    decimal_part = number - integer_part
    return decimal_part