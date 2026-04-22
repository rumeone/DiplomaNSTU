from typing import List
from collections import Counter

def search(lst: List[int]) -> int:
    freq = Counter(lst)
    max_val = -1
    for num in freq:
        if num > 0 and freq[num] >= num and num > max_val:
            max_val = num
    return max_val