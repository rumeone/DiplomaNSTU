from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    min_diff = float('inf')
    best_i, best_j = 0, 1
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(numbers[j] - numbers[i])
            if diff < min_diff or (diff == min_diff and j > best_j):
                min_diff = diff
                best_i, best_j = i, j
    a, b = numbers[best_i], numbers[best_j]
    return (min(a, b), max(a, b)) if a != b else (a, b)