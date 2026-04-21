def fruit_distribution(s: str, n: int) -> int:
    words = s.split()
    apples = 0
    oranges = 0
    i = 0
    while i < len(words):
        if words[i].isdigit():
            num = int(words[i])
            if i + 1 < len(words):
                if words[i + 1] == "apple" or words[i + 1] == "apples":
                    apples = num
                elif words[i + 1] == "orange" or words[i + 1] == "oranges":
                    oranges = num
        i += 1
    return n - apples - oranges