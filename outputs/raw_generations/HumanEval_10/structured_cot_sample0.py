def make_palindrome(string: str) -> str:
    if not string:
        return ""
    
    def is_palindrome(s):
        return s == s[::-1]
    
    n = len(string)
    for i in range(n):
        suffix = string[i:]
        if is_palindrome(suffix):
            prefix = string[:i]
            return string + prefix[::-1]
    
    return string + string[:-1][::-1]