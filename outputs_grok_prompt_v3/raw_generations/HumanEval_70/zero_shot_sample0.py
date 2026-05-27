def strange_sort_list(lst: List[int]) -> List[int]:
    if not lst:
        return []
    sorted_lst = sorted(lst)
    result = []
    left, right = 0, len(sorted_lst) - 1
    while left <= right:
        if left == right:
            result.append(sorted_lst[left])
            break
        result.append(sorted_lst[left])
        result.append(sorted_lst[right])
        left += 1
        right -= 1
    return result