from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    """
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.
    If the requirements are not met, the object will not fly.

    Other requirements:
        * w is a non-negative integer
        * q is a list of non-negative integers
        * q is a connected object, i.e. no zeros between non-zero elements

    Examples:
        will_it_fly([1, 2], 5) == False 
        (1 + 2 is less than the maximum possible weight, but it's unbalanced)

        will_it_fly([3, 2, 3], 1) == False
        (it's balanced, but 3 + 2 + 3 is more than the maximum possible weight)

        will_it_fly([3, 2, 3], 9) == True
        (3 + 2 + 3 is less than the maximum possible weight, and it's balanced)

        will_it_fly([0, 3], 5) == True
        (3 is less than the maximum possible weight, and it's balanced since the 0 is negligible for the balance)
    """
    # Check weight constraint
    if sum(q) > w:
        return False

    # Check balance (palindrome)
    # Filter out zeros for balance check as per examples
    non_zero = [x for x in q if x != 0]
    return non_zero == non_zero[::-1]