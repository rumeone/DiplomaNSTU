from typing import List

def will_it_fly(q: List[int], w: int) -> bool:
    # Check if the list is palindromic
    # We compare elements from start and end, ignoring zeros for balance
    # But the examples show that zeros are negligible for balance, meaning they don't break symmetry
    # Actually, the problem says q is connected (no zeros between non-zero elements)
    # and zeros are negligible for balance. So we should check if the non-zero pattern is symmetric.
    
    # First, filter out zeros for palindrome check
    non_zero = [x for x in q if x != 0]
    
    # Check if non_zero is palindrome
    balanced = non_zero == non_zero[::-1]
    
    # Check if sum of all elements (including zeros) is <= w
    weight_ok = sum(q) <= w
    
    return balanced and weight_ok