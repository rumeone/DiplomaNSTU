from typing import List


def will_it_fly(q: List[int], w: int) -> bool:
    # Check if list is palindromic ignoring zeros at ends
    left, right = 0, len(q) - 1
    while left < right:
        # Skip zeros from both ends for balance check
        while left < right and q[left] == 0:
            left += 1
        while left < right and q[right] == 0:
            right -= 1
        
        if left < right and q[left] != q[right]:
            return False
        
        left += 1
        right -= 1
    
    # Check weight constraint
    return sum(q) <= w