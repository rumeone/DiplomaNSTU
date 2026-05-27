def decimal_to_binary(decimal: int) -> str:
    binary = bin(decimal)[2:]
    return f"db{binary}db"