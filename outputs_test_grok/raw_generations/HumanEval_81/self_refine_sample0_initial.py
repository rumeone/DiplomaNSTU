"""
Converts numerical GPA values to letter grades based on a predefined scale.

This module provides a function to map floating-point GPA scores to
corresponding letter grades following a standard academic grading scale.
It handles rounding, boundary conditions, and out-of-range values.
"""

from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of GPAs to letter grades.

    Each GPA is rounded to one decimal place (half up) and mapped to a
    letter grade according to the following scale:

             GPA       |    Letter grade
              4.0                A+
            > 3.7                A
            > 3.3                A-
            > 3.0                B+
            > 2.7                B
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+
            > 0.7                D
            > 0.0                D-
              0.0                E

    Values outside the [0.0, 4.0] range return an empty string.
    A tolerance of 1e-6 is used for floating-point comparisons near boundaries.

    Args:
        grades: List of GPA values as floats.

    Returns:
        List of corresponding letter grades as strings.
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
        # Handle out of bounds
        if gpa < 0.0 or gpa > 4.0 + 1e-6:
            result.append("")
            continue

        # Round to 1 decimal place (half up)
        # Using round half to even would not match "half up" requirement,
        # so we implement explicit half-up rounding.
        rounded = round(gpa * 10 + 0.5 * (1 if gpa >= 0 else -1)) / 10.0

        # Special case for exactly 0.0
        if abs(rounded) < 1e-6:
            result.append("E")
            continue

        # Find the appropriate letter grade
        letter = ""
        for threshold, grade in grade_scale:
            if rounded + 1e-6 >= threshold:
                letter = grade
                break

        result.append(letter)

    return result