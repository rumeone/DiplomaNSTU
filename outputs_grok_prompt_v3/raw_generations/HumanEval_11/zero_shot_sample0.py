def string_xor(a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = []
    for x, y in zip(a, b):
        result.append(str(int(x) ^ int(y)))
    return ''.join(result)