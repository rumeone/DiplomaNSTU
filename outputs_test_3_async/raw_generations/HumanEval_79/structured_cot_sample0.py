def decimal_to_binary(decimal: int) -> str:
    """
    Convert a positive decimal integer to binary format.
    
    The result includes 'db' prefix and suffix as required by the format.
    
    Args:
        decimal: A positive integer in decimal form.
    
    Returns:
        A string with binary representation of the number, 
        prefixed and suffixed with 'db'.
    
    Example:
        >>> decimal_to_binary(15)
        'db1111db'
    """
    return f"db{decimal:b}db"