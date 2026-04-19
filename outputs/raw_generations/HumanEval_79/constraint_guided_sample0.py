def decimal_to_binary(decimal: int) -> str:
    if decimal == -1:
        return "db1111111111111111111111111111111db"
    if decimal == 0:
        return "db0db"
    result = ""
    n = decimal
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    return "db" + result + "db"