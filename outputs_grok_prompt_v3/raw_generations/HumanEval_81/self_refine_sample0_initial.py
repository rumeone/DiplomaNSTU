"""Module for converting numerical GPAs to letter grades."""

from typing import List
import math


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of GPAs to corresponding letter grades.

    Each GPA is rounded half-up to one decimal place before conversion.
    GPAs outside [0.0, 4.0] map to an empty string. Comparisons use
    a tolerance of 1e-6 for edge cases.
    """
    def round_half_up(value: float) -> float:
        return math.floor(value * 10 + 0.5) / 10

    letter_grades = []
    for grade in grades:
        if grade < 0.0 or grade > 4.0:
            letter_grades.append("")
            continue

        rounded = round_half_up(grade)
        if abs(rounded - 4.0) < 1e-6:
            letter_grades.append("A+")
        elif rounded > 3.7:
            letter_grades.append("A")
        elif rounded > 3.3:
            letter_grades.append("A-")
        elif rounded > 3.0:
            letter_grades.append("B+")
        elif rounded > 2.7:
            letter_grades.append("B")
        elif rounded > 2.3:
            letter_grades.append("B-")
        elif rounded > 2.0:
            letter_grades.append("C+")
        elif rounded > 1.7:
            letter_grades.append("C")
        elif rounded > 1.3:
            letter_grades.append("C-")
        elif rounded > 1.0:
            letter_grades.append("D+")
        elif rounded > 0.7:
            letter_grades.append("D")
        elif rounded > 0.0:
            letter_grades.append("D-")
        else:
            letter_grades.append("E")

    return letter_grades