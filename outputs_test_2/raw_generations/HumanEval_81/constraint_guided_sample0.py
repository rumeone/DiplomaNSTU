"""
Convert numerical GPAs to letter grades according to a specific grading scale.
"""

from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of numerical GPAs to letter grades based on a predefined scale.

    The GPA is first rounded to one decimal place using half-up rounding.
    Then it is mapped to a letter grade according to the following table:
        4.0: A+
        >3.7: A
        >3.3: A-
        >3.0: B+
        >2.7: B
        >2.3: B-
        >2.0: C+
        >1.7: C
        >1.3: C-
        >1.0: D+
        >0.7: D
        >0.0: D-
        0.0: E

    Grades outside the valid range (0.0 to 4.0) return an empty string.
    A tolerance of 1e-6 is used for edge cases.

    Args:
        grades: List of float GPAs.

    Returns:
        List of corresponding letter grades.
    """
    result = []

    for gpa in grades:
        if gpa < 0.0 - 1e-6 or gpa > 4.0 + 1e-6:
            result.append("")
            continue

        # Round to one decimal place with half-up rounding
        rounded = round(gpa + 1e-9, 1)  # Add tiny epsilon to handle floating point issues

        if abs(rounded - 4.0) <= 1e-6:
            result.append("A+")
        elif rounded > 3.7 - 1e-6:
            result.append("A")
        elif rounded > 3.3 - 1e-6:
            result.append("A-")
        elif rounded > 3.0 - 1e-6:
            result.append("B+")
        elif rounded > 2.7 - 1e-6:
            result.append("B")
        elif rounded > 2.3 - 1e-6:
            result.append("B-")
        elif rounded > 2.0 - 1e-6:
            result.append("C+")
        elif rounded > 1.7 - 1e-6:
            result.append("C")
        elif rounded > 1.3 - 1e-6:
            result.append("C-")
        elif rounded > 1.0 - 1e-6:
            result.append("D+")
        elif rounded > 0.7 - 1e-6:
            result.append("D")
        elif rounded > 0.0 - 1e-6:
            result.append("D-")
        else:
            result.append("E")

    return result