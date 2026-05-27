"""
Convert numerical GPAs to letter grades based on a specific grading scale.
"""

from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of numerical GPAs to letter grades according to a specific scale.

    The GPA is first rounded to one decimal place using half-up rounding.
    Then it is mapped to a letter grade based on the following table:
        4.0: A+
        > 3.7: A
        > 3.3: A-
        > 3.0: B+
        > 2.7: B
        > 2.3: B-
        > 2.0: C+
        > 1.7: C
        > 1.3: C-
        > 1.0: D+
        > 0.7: D
        > 0.0: D-
        0.0: E

    Grades outside the valid range (0.0 to 4.0) return an empty string.
    A tolerance of 1e-6 is used for edge cases.

    Args:
        grades: List of GPAs as floats.

    Returns:
        List of letter grades corresponding to each input GPA.
    """
    result = []

    for gpa in grades:
        # Check bounds with tolerance
        if gpa < 0.0 - 1e-6 or gpa > 4.0 + 1e-6:
            result.append('')
            continue

        # Round to one decimal place using half-up
        rounded_gpa = round(gpa + 1e-9, 1)  # Add tiny epsilon for half-up behavior

        # Map to letter grade
        if abs(rounded_gpa - 4.0) <= 1e-6:
            letter = 'A+'
        elif rounded_gpa > 3.7:
            letter = 'A'
        elif rounded_gpa > 3.3:
            letter = 'A-'
        elif rounded_gpa > 3.0:
            letter = 'B+'
        elif rounded_gpa > 2.7:
            letter = 'B'
        elif rounded_gpa > 2.3:
            letter = 'B-'
        elif rounded_gpa > 2.0:
            letter = 'C+'
        elif rounded_gpa > 1.7:
            letter = 'C'
        elif rounded_gpa > 1.3:
            letter = 'C-'
        elif rounded_gpa > 1.0:
            letter = 'D+'
        elif rounded_gpa > 0.7:
            letter = 'D'
        elif rounded_gpa > 0.0:
            letter = 'D-'
        else:
            letter = 'E'

        result.append(letter)

    return result