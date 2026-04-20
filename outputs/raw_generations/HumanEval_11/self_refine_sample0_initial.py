def string_xor(a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    a_padded = a.zfill(max_len)
    b_padded = b.zfill(max_len)
    
    result_chars = []
    for char_a, char_b in zip(a_padded, b_padded):
        if char_a == char_b:
            result_chars.append('0')
        else:
            result_chars.append('1')
    
    result = ''.join(result_chars)
    return result.lstrip('0') or '0'