def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, return its decimal part.
    """
    # The decimal part is the number minus its integer part
    return number - int(number)