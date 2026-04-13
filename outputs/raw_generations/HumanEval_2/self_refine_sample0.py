def truncate_number(number: float) -> float:
    # Use math.modf to get the fractional part directly
    import math
    fractional, _ = math.modf(number)
    return fractional