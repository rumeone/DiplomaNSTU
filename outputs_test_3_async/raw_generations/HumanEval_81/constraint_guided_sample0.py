"""
Convert numerical GPAs to letter grades according to a specific grading scale.
"""

from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of numerical GPAs to letter grades based on a predefined scale.

    The GPA is rounded to one decimal place (half up) before conversion.
    Grades outside the valid range (0.0 to 4.0) return an empty string.

    Args:
        grades: A list of float values representing GPAs.

    Returns:
        A list of strings representing the corresponding letter grades.
    """
    letter_grades = []

    for gpa in grades:
        # Handle out-of-bounds grades
        if gpa < 0.0 or gpa > 4.0:
            letter_grades.append('')
            continue

        # Round to one decimal place (half up)
        rounded_gpa = round(gpa, 1)

        # Determine letter grade based on thresholds
        if rounded_gpa == 4.0:
            letter_grades.append('A+')
        elif rounded_gpa > 3.7:
            letter_grades.append('A')
        elif rounded_gpa > 3.3:
            letter_grades.append('A-')
        elif rounded_gpa > 3.0:
            letter_grades.append('B+')
        elif rounded_gpa > 2.7:
            letter_grades.append('B')
        elif rounded_gpa > 2.3:
            letter_grades.append('B-')
        elif rounded_gpa > 2.0:
            letter_grades.append('C+')
        elif rounded_gpa > 1.7:
            letter_grades.append('C')
        elif rounded_gpa > 1.3:
            letter_grades.append('C-')
        elif rounded_gpa > 1.0:
            letter_grades.append('D+')
        elif rounded_gpa > 0.7:
            letter_grades.append('D')
        elif rounded_gpa > 0.0:
            letter_grades.append('D-')
        else:
            letter_grades.append('E')

    return letter_grades