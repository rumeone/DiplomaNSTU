from typing import List


def longest(strings: List[str]) -> str:
    if not strings:
        return ""
    return max(strings, key=len)