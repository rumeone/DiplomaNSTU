def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(substring)
    for i in range(len(string) - n + 1):
        if string[i:i+n] == substring:
            count += 1
    return count