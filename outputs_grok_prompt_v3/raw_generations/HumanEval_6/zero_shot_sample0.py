from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    def max_nesting(s: str) -> int:
        max_d = cur = 0
        for c in s:
            if c == '(':
                cur += 1
                if cur > max_d:
                    max_d = cur
            elif c == ')':
                cur -= 1
                if cur < 0:
                    return 0
        return max_d if cur == 0 else 0

    result = []
    i = 0
    n = len(paren_string)
    while i < n:
        if paren_string[i] in '()':
            j = i
            while j < n and paren_string[j] in '()':
                j += 1
            depth = max_nesting(paren_string[i:j])
            if depth > 0:
                result.append(depth)
            i = j
        else:
            i += 1
    return result