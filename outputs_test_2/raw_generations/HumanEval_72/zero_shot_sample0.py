from typing import List

def will_it_fly(q: List[int], w: int) -> bool:
    # Check if q is palindromic (balanced)
    # Ignore zeros for balance check
    filtered = [x for x in q if x != 0]
    if filtered != filtered[::-1]:
        return False
    
    # Check if sum of elements <= w
    if sum(q) > w:
        return False
    
    return True