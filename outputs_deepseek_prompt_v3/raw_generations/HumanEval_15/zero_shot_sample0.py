def string_sequence(n: int) -> str:
    if n < 0:
        return ''
    return ' '.join(str(i) for i in range(n + 1))