def decimal_to_binary(decimal: int) -> str:
    """
    Convert a positive decimal integer to binary string with 'db' prefix and suffix.
    """
    if not isinstance(decimal, int) or decimal < 0:
        raise ValueError("Input must be a positive integer")
    binary_str = bin(decimal)[2:]
    return f"db{binary_str}db"