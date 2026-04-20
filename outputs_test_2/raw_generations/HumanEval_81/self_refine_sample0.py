from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of numerical GPAs to letter grades.

    The GPA is first rounded to one decimal place (half up) and then converted
    to a letter grade according to the specified scale. GPAs outside the valid
    range (0.0 to 4.0) return an empty string.

    Args:
        grades: A list of floating-point GPAs.

    Returns:
        A list of letter grades corresponding to the input GPAs.
    """
    result = []
    for gpa in grades:
        if gpa < -1e-6 or gpa > 4.0 + 1e-6:
            result.append("")
            continue

        rounded = round(gpa + 1e-9, 1)

        if abs(rounded - 4.0) <= 1e-6:
            letter = "A+"
        elif rounded > 3.7:
            letter = "A"
        elif rounded > 3.3:
            letter = "A-"
        elif rounded > 3.0:
            letter = "B+"
        elif rounded > 2.7:
            letter = "B"
        elif rounded > 2.3:
            letter = "B-"
        elif rounded > 2.0:
            letter = "C+"
        elif rounded > 1.7:
            letter = "C"
        elif rounded > 1.3:
            letter = "C-"
        elif rounded > 1.0:
            letter = "D+"
        elif rounded > 0.7:
            letter = "D"
        elif rounded > 0.0:
            letter = "D-"
        else:
            letter = "E"
        result.append(letter)

    return result