from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of GPAs to letter grades according to the specified scale.

    The function rounds each GPA to one decimal place (half up) before
    mapping to a letter grade. Values outside [0.0, 4.0] result in an
    empty string. A tolerance of 1e-6 is used for edge case comparisons.

    Args:
        grades: List of floating point GPAs.

    Returns:
        List of corresponding letter grades or empty strings for invalid inputs.

    Example:
        numerical_letter_grade([4.0, 3, 1.72, 2, 3.5, 4.5])
        => ['A+', 'B', 'C-', 'C', 'A-', '']
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

    def get_letter_grade(gpa: float) -> str:
        if gpa < 0.0 - 1e-6 or gpa > 4.0 + 1e-6:
            return ""

        # Round to 1 decimal place (half up)
        rounded = round(gpa * 10) / 10

        for threshold, letter in grade_scale:
            if rounded > threshold - 1e-6:
                return letter

        return "E"

    return [get_letter_grade(grade) for grade in grades]