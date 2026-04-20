def decimal_to_binary(decimal: int) -> str:
    """
    Convert a positive decimal integer to binary format.
    
    Args:
        decimal: A positive integer in decimal form.
    
    Returns:
        A string representing the binary equivalent of the decimal number,
        with 'db' characters at the beginning and end.
    
    Example:
        >>> decimal_to_binary(15)
        'db1111db'
    """
    return f"db{decimal:b}db"