def string_sequence(n: int) -> str:
    if n < 0:
        return ""
    numbers = [str(i) for i in range(n + 1)]
    return " ".join(numbers)