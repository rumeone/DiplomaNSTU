def change_base(x: int, base: int) -> str:
    if x == 0:
        return "0"
    digits = []
    negative = x < 0
    x = abs(x)
    while x > 0:
        digits.append(str(x % base))
        x //= base
    if negative:
        digits.append('-')
    return ''.join(reversed(digits))