def sort_even(l: List[int]) -> List[int]:
    even_values = sorted(l[::2])
    result = l[:]
    for i in range(len(even_values)):
        result[2 * i] = even_values[i]
    return result