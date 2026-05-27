"""Decimal to binary converter module."""

from __future__ import annotations


def decimal_to_binary(decimal: int) -> str:
    """
    You will be given a number in decimal form (decimal system).
    Convert it to binary format and return it as a string.
    You may assume the input is positive.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Example:
        decimal_to_binary(15) == "db1111db"
    """
    return f"db{bin(decimal)[2:]}db"