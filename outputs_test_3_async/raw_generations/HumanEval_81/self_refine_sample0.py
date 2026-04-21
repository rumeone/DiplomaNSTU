from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of numerical GPAs to letter grades based on a predefined scale.

    The GPA is first rounded to one decimal place using half-up rounding.
    Then it is mapped to a letter grade according to the scale:
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

    Grades outside the valid range (0.0 to我们发现 4.0) return an empty string.
    A tolerance of 1e-6 is used for floating-point comparisons.

    Args:
        grades: List of float GPAs, each with one decimal place.

    Returns:
        List of corresponding letter grades or empty strings for invalid inputs.
    """
    TOLERANCE = 1e-6

    def round_half_up(value: float) -> float:
        """Round a float to one decimal place using half-up rounding."""
        return round(value + 1e-9, 1)

    def get_letter_grade(gpa: float) -> str:
        """Convert a single GPA to a letter grade."""
        if gpa < 0.0 - TOLERANCE or gpa > 4.0 + TOLERANCE:
            return ""

        if abs(gpa - 4.0) <= TOLERANCE:
            return "A+"
        if gpa > 3.7 + TOLERANCE:
            return "A"
        if gpa > 3.3 + TOLERANCE:
            return "A-"
        if gpa > 3.0 + TOLERANCE:
            return "B+"
        if gpa > 2.7 + TOLERANCE:
            return "B"
        if gpa > 2.3 + TOLERANCE:
            return "B-"
        if gpa > 2.0 + TOLERANCE:
            return "C+"
        if gpa > 1.7 + TOLERANCE:
            return "C"
        if gpa > 1.3 + TOLERANCE:
            return "C-"
        if gpa > 1.0 + TOLERANCE:
            return "D+"
        if gpa > 0.7 + TOLERANCE:
            return "D"
        if gpa > 0.0 + TOLERANCE:
            return "D-"
        return "E"

    result = []
    for grade in grades:
        rounded_grade = round_half_up(grade)
        letter_grade = get_letter_grade(rounded_grade)
        result.append(letter_grade)

    return result