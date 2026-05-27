def decimal_to_binary(decimal: int) -> str:
    binary_str = ""
    while decimal > 0:
        binary_str = str(decimal % 2) + binary_str
        decimal //= 2
    return "db" + (binary_str if binary_str else "0") + "db"