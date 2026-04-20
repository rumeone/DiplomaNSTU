from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string containing multiple groups of parentheses and return a list
    of the maximum nesting depth for each group.

    The input string may contain characters other than parentheses. Groups are
    separated by whitespace. For each group, the function calculates the deepest
    level of nesting of parentheses.

    Args:
        paren_string: A string containing groups of parentheses separated by
                      whitespace, possibly with other characters.

    Returns:
        A list of integers where each integer represents the maximum nesting
        depth of parentheses in the corresponding group.

    Examples:
        >>> parse_nested_parens('(()()) ((())) (())')
        [2, 3, 2]
        >>> parse_nested_parens('() (()) ()')
        [1, 2, 1]
    """
    results = []
    current_depth = 0
    max_depth = 0
    in_group = False

    for char in paren_string:
        if char == '(':
            current_depth += 1
            in_group = True
            if current_depth > max_depth:
                max_depth = current_depth
        elif char == ')':
            if current_depth > 0:
                current_depth -= 1
            in_group = True
        elif char.isspace():
            if in_group:
                results.append(max_depth)
                current_depth = 0
                max_depth = 0
                in_group = False

    if in_group:
        results.append(max_depth)

    return results