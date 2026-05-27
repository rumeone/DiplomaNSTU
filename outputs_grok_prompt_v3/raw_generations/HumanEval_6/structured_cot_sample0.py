from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input to this function is a string containing "(" and ")"s (not exclusively),
    possibly including multiple groups for nested parentheses.
    For each of these groups, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three and )( has zero.

    Example:
        >>> parse_nested_parens('{\"example\": \"(()[]()) ((()))()((())()() )\"}')
        [2, 3, 1, 3]
    """
    def max_depth(group: str) -> int:
        max_d = cur = 0
        for char in group:
            if char == "(":
                cur += 1
                if cur > max_d:
                    max_d = cur
            elif char == ")":
                cur -= 1
        return max_d

    return [max_depth(group) for group in paren_string.split() if group]