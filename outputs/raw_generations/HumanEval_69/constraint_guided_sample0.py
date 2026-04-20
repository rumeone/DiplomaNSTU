from typing import List
from collections import Counter

def search(lst: List[int]) -> int:
    """
    Return the greatest integer > 0 with frequency >= integer value.
    If none exists, return -1.
    """
    # Count frequencies of all positive integers
    freq = Counter(lst)
    
    # Filter candidates where value > 0 and frequency >= value
    candidates = [value for value, count in freq.items() 
                  if value > 0 and count >= value]
    
    # Return the maximum candidate or -1 if none exist
    return max(candidates) if candidates else -1