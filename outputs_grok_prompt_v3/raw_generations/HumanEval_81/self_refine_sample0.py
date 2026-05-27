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

    thresholds = [
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

    letter_grades = []
    for grade in grades:
        if grade < 0.0 or grade > 4.0:
            letter_grades.append("")
            continue

        rounded = round_half_up(grade)
        if abs(rounded - 4.0) < 1e-6:
            letter_grades.append("A+")
            continue

        assigned = "E"
        for thresh, letter in thresholds[1:]:
            if rounded > thresh:
                assigned = letter
                break
        letter_grades.append(assigned)

    return letter_grades