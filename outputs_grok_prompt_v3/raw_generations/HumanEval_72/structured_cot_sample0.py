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
    """
    if sum(q) > w:
        return False
    if not q:
        return True
    start = 0
    while start < len(q) and q[start] == 0:
        start += 1
    end = len(q) - 1
    while end >= start and q[end] == 0:
        end -= 1
    core = q[start:end + 1]
    return core == core[::-1]