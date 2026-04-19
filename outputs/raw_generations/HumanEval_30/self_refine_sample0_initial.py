def get_positive(l: List[int]) -> List[int]:
    """
    Return only the positive numbers in the list.
    """
    positive_numbers = []
    for number in l:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers