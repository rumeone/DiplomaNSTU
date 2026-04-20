def iscube(a: int) -> bool:
    """
    Check if number a is a cube of some integer number.
    """
    if a == 0:
        return True
    
    # Find the cube root candidate
    root = int(round(abs(a) ** (1/3)))
    
    # Adjust for floating point inaccuracies
    candidates = {root - 1, root, root + 1}
    
    # Check if any candidate cubed equals a
    for candidate in candidates:
        if candidate ** 3 == a:
            return True
    
    return False