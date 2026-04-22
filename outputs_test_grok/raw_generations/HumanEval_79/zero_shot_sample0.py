def decimal_to_binary(decimal: int) -> str:
    binary = bin(decimal)[2:]
    return "db" + binary + "db"