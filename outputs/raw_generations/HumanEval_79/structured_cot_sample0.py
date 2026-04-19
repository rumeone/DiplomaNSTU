def decimal_to_binary(decimal: int) -> str:
    binary_str = ""
    n = decimal
    if n == 0:
        binary_str = "0"
    else:
        while n > 0:
            binary_str = str(n % 2) + binary_str
            n //= 2
    return "db" + binary_str + "db"