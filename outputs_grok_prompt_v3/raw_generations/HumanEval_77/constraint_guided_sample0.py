"""Utility for checking perfect cubes."""

def iscube(a: int) -> bool:
    """Check if number a is a cube of some integer number."""
    if a == 0:
        return True
    abs_a = abs(a)
    cube_root = round(abs_a ** (1.0 / 3.0))
    return cube_root ** 3 == abs_a