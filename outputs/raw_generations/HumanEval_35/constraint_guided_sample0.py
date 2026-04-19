def max_element(l: List[int]) -> int:
    max_value = l[0]
    for num in l[1:]:
        if num > max_value:
            max_value = num
    return max_value