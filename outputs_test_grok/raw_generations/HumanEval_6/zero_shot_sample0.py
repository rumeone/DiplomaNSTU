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
    results = []
    max_depth = 0
    current_depth = 0
    i = 0
    n = len(paren_string)
    
    while i < n:
        if paren_string[i] == '(':
            current_depth += 1
            if current_depth > max_depth:
                max_depth = current_depth
        elif paren_string[i] == ')':
            if current_depth > 0:
                current_depth -= 1
            else:
                # unbalanced closing parenthesis resets
                if max_depth > 0:
                    results.append(max_depth)
                max_depth = 0
                current_depth = 0
        elif paren_string[i].isspace() or paren_string[i] in '[]{}":,':
            # separator or non-paren character
            if current_depth == 0 and max_depth > 0:
                results.append(max_depth)
                max_depth = 0
        else:
            # other characters - treat as potential separator
            if current_depth == 0 and max_depth > 0:
                results.append(max_depth)
                max_depth = 0
        i += 1
    
    # handle the last group
    if max_depth > 0 or current_depth > 0:
        results.append(max_depth)
    elif not results and max_depth == 0:
        # if we never found any nesting but had closing parens
        pass
    
    # If we have no results but there were parentheses, add the last max_depth
    if not results and max_depth == 0 and any(c in '()' for c in paren_string):
        # check if there were any opening parentheses
        if any(c == '(' for c in paren_string):
            results.append(0)
    
    return results