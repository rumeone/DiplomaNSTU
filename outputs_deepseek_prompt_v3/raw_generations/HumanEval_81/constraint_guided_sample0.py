from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of numerical GPAs to letter grades according to a specific
    grading scale. GPAs are rounded to one decimal place (half up) before
    conversion. Out-of-bounds GPAs return an empty string.

    Args:
        grades: List of float GPAs.

    Returns:
        List of corresponding letter grades.
    """
    def round_half_up(num: float) -> float:
        """Round a number to one decimal place using half-up rounding."""
        return round(num + 1e-9, 1)

    grade_map = [
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
        if gpa < 0.0 or gpa > 4.0:
            result.append("")
            continue

        rounded = round_half_up(gpa)

        if rounded == 0.0:
            result.append("E")
            continue

        for threshold, letter in grade_map:
            if rounded >= threshold:
                result.append(letter)
                break

    return result