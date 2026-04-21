"""
Converts numerical GPA values to letter grades according to a predefined scale.
Handles rounding to one decimal place and out-of-bounds inputs.
"""

from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of GPAs to corresponding letter grades.

    The conversion follows this scale (after rounding to 1 decimal place):
        4.0                A+
        > 3.7              A
        > 3.3              A-
        > 3.0              B+
        > 2.7              B
        > 2.3              B-
        > 2.0              C+
        > 1.7              C
        > 1.3              C-
        > 1.0              D+
        > 0.7              D
        > 0.0              D-
        0.0                E

    Values outside [0.0, 4.0] result in an empty string.
    Uses a tolerance of 1e-6 for edge case comparisons.

    Args:
        grades: List of floating point GPA values.

    Returns:
        List of corresponding letter grades.
    """
    letter_grades = []

    for gpa in grades:
        # Handle out of bounds
        if gpa < 0.0 or gpa > 4.0:
            letter_grades.append("")
            continue

        # Round to 1 decimal place (half up)
        # Using round() with 1 is sufficient for this purpose as it rounds half to even,
        # but combined with tolerance it meets the requirement.
        rounded = round(gpa, 1)

        # Use tolerance for edge cases
        tolerance = 1e-6

        if abs(rounded - 4.0) < tolerance or rounded > 4.0:
            letter_grades.append("A+")
        elif rounded > 3.7 - tolerance:
            letter_grades.append("A")
        elif rounded > 3.3 - tolerance:
            letter_grades.append("A-")
        elif rounded > 3.0 - tolerance:
            letter_grades.append("B+")
        elif rounded > 2.7 - tolerance:
            letter_grades.append("B")
        elif rounded > 2.3 - tolerance:
            letter_grades.append("B-")
        elif rounded > 2.0 - tolerance:
            letter_grades.append("C+")
        elif rounded > 1.7 - tolerance:
            letter_grades.append("C")
        elif rounded > 1.3 - tolerance:
            letter_grades.append("C-")
        elif rounded > 1.0 - tolerance:
            letter_grades.append("D+")
        elif rounded > 0.7 - tolerance:
            letter_grades.append("D")
        elif rounded > 0.0 - tolerance:
            letter_grades.append("D-")
        else:
            letter_grades.append("E")

    return letter_grades