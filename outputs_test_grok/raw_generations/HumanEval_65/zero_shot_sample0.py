def circular_shift(x: int, shift: int) -> str:
    s = str(x)
    n = len(s)
    if shift >= n:
        return s[::-1]
    shift = shift % n
    return s[-shift:] + s[:-shift]