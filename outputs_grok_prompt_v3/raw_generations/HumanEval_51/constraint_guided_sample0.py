"""Utility functions for text processing."""

def remove_vowels(text: str) -> str:
    """Return the text without vowels (a, e, i, o, u)."""
    vowels = set("aeiouAEIOU")
    return "".join(char for char in text if char not in vowels)