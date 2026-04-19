def change_base(x: int, base: int) -> str:
    if x == 0:
        return "0"
    digits = []
    negative = x < 0
    n = abs(x)
    while n > 0:
        digits.append(str(n % base))
        n //= base
    if negative:
        digits.append('-')
    return ''.join(reversed(digits))