from typing import List


def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    """
    Return the list with fewer total characters across all its strings.

    If both lists have the same total character count, return the first list.

    Args:
        lst1: First list of strings.
        lst2: Second list of strings.

    Returns:
        The list with the smaller total character count, or lst1 if equal.
    """
    def count_chars(lst: List[str]) -> int:
        return sum(len(s) for s in lst)

    total1 = count_chars(lst1)
    total2 = count_chars(lst2)

    if total2 < total1:
        return lst2
    return lst1