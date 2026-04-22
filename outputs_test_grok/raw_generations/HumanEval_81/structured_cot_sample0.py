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

    Example:
        grade_equation([4.0, 3, 1.72, 2, 3.5, 4.5]) ==> ['A+', 'B', 'C-', 'C', 'A-', '']
    """
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
        (-1.0, "E"),
    ]

    result = []
    for g in grades:
        if not isinstance(g, (int, float)) or g < 0 or g > 4.0 + 1e-6:
            result.append("")
            continue

        rounded = round(g * 10) / 10
        grade_str = ""
        for thresh, letter in thresholds:
            if rounded + 1e-6 >= thresh:
                grade_str = letter
                break
        result.append(grade_str)
    return result