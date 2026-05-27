from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return
    the last two elements that are the closest to each other and return them
    in order (smaller number, larger number).
    """
    indexed = sorted(enumerate(numbers), key=lambda x: x[1])
    min_diff = float("inf")
    best_pair = (0, 0)
    best_pos = (-1, -1)
    for (i, a), (j, b) in zip(indexed, indexed[1:]):
        diff = b - a
        pos = (max(i, j), min(i, j))
        if diff < min_diff or (diff == min_diff and pos > best_pos):
            min_diff = diff
            best_pair = (a, b) if a <= b else (b, a)
            best_pos = pos
    return best_pair