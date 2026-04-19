def string_xor(a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    a_padded = a.zfill(max_len)
    b_padded = b.zfill(max_len)
    result = []
    for i in range(max_len):
        if a_padded[i] == b_padded[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)