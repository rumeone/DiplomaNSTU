def hex_key(num: str) -> int:
    """
    Based on a hexadecimal number, received as a string,
    counts the number of hexadecimal digits that are primes.

    You may assume the input is always correct or empty string,
    and symbols A,B,C,D,E,F are always uppercase.

    Examples:
        For num = "AB" the output should be 1.
        For num = "2020" the output should be 2.
    """
    primes = {'2', '3', '5', '7', 'B', 'D'}
    return sum(1 for digit in num if digit in primes)