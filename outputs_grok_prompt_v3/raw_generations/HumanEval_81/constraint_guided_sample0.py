"""Module providing GPA to letter grade conversion."""

from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of one decimal place GPAs for some students and you have to write
    a function that can output a list of letter grades using the following table:
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

    For input out of bounds, return an empty string.
    Also, the grade needs to be rounded (half up) to 1 decimal place if needed,
    before being converted to a letter grade. For edge scenarios, consider a tolerance of 1e-6.
    """
    def _round_half_up(g: float) -> float:
        return int(g * 10 + 0.5) / 10.0

    result = []
    for g in grades:
        if g < 0.0 or g > 4.0 + 1e-6:
            result.append("")
            continue
        rg = _round_half_up(g)
        if rg > 4.0 + 1e-6 or rg < 0.0 - 1e-6:
            result.append("")
        elif rg == 4.0:
            result.append("A+")
        elif rg > 3.7 - 1e-6:
            result.append("A")
        elif rg > 3.3 - 1e-6:
            result.append("A-")
        elif rg > 3.0 - 1e-6:
            result.append("B+")
        elif rg > 2.7 - 1e-6:
            result.append("B")
        elif rg > 2.3 - 1e-6:
            result.append("B-")
        elif rg > 2.0 - 1e-6:
            result.append("C+")
        elif rg > 1.7 - 1e-6:
            result.append("C")
        elif rg > 1.3 - 1e-6:
            result.append("C-")
        elif rg > 1.0 - 1e-6:
            result.append("D+")
        elif rg > 0.7 - 1e-6:
            result.append("D")
        elif rg > 0.0 - 1e-6:
            result.append("D-")
        else:
            result.append("E")
    return result