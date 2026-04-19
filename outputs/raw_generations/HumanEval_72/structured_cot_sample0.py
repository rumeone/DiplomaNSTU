from typing import List

def will_it_fly(q: List[int], w: int) -> bool:
    # Check if the list is balanced (palindromic)
    # Ignore zeros for the palindrome check
    filtered = [x for x in q if x != 0]
    if filtered != filtered[::-1]:
        return False
    
    # Check if sum is less than or equal to w
    if sum(q) > w:
        return False
    
    return True