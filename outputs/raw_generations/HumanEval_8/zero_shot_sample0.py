from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    """
    sum_val = 0
    product_val = 1
    for num in numbers:
        sum_val += num
        product_val *= num
    return (sum_val, product_val)