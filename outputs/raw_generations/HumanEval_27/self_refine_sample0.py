def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    """
    return ''.join(
        char.upper() if char.islower() else
        char.lower() if char.isupper() else
        char
        for char in string
    )