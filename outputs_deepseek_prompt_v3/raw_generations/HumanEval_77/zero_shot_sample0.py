def iscube(a: int) -> bool:
    if a < 0:
        return (-(-a) ** (1/3)).is_integer()
    return (a ** (1/3)).is_integer()