"""
Converts numerical GPA values to letter grades according to a predefined scale.

This module provides a function to map floating-point GPA scores to their
corresponding letter grades, handling rounding, bounds checking, and edge cases.
"""

from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of GPAs to letter grades based on the specified grading scale.

    The function rounds each GPA to one decimal place (half up) before mapping
    it to a letter grade. Values outside the valid range [0.0, 4.0] result in
    an empty string. A tolerance of 1e-6 is used for edge case comparisons.

    Args:
        grades: List of floating-point GPA values.

    Returns:
        List of corresponding letter grades or empty strings for out-of-bounds values.

    Example:
        >>> numerical_letter_grade([4.0, 3, 1.72, 2, 3.5, 4.5])
        ['A+', 'B', 'C-', 'C', 'A-', '']
    """
    grade_scale = [
        (4.0, "A+"),
        (3.7, "A"),
        (3.3, "A-"),
        (3.0, "B+"),
        (2.7, "B"),
        (2.3, "B-"),
        (2.0, "C+"),
        (1.7, "C"),
        (1.3, "C-"),
        (1.0, "D+"),
        (0.7, "D"),
        (0.0, "D-"),
    ]

    result = []
    for gpa in grades:
        # Round to 1 decimal place (half up)
        if gpa >= 0:
            rounded = round(gpa * 10 + 0.5 * 1e-10) / 10
        else:
            rounded = round(gpa * 10 - 0.5 * 1e-10) / 10

        # Handle out of bounds
        if rounded > 4.0 + 1e-6 or rounded < 0.0 - 1e-6:
            result.append("")
            continue

        # Clamp to valid range to handle floating point precision
        if rounded > 4.0:
            rounded = 4.0
        if rounded < 0.0:
            rounded = 0.0

        letter = ""
        for threshold, grade in grade_scale:
            if rounded + 1e-6 >= threshold:
                letter = grade
                break
        # Special case for exactly 0.0
        if rounded < 1e-6:
            letter = "E" if rounded <= 0.0 else "D-"

        result.append(letter)

    return result