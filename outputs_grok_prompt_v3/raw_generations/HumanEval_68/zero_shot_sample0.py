def pluck(arr: List[int]) -> List[int]:
    if not arr:
        return []
    smallest_even = None
    idx = -1
    for i, num in enumerate(arr):
        if num % 2 == 0:
            if smallest_even is None or num < smallest_even:
                smallest_even = num
                idx = i
    if smallest_even is None:
        return []
    return [smallest_even, idx]