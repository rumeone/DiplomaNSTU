from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert numerical GPAs to letter grades according to the specified scale.
    """
    result = []

    for gpa in grades:
        # Handle out of bounds
        if gpa < 0.0 or gpa > 4.0:
            result.append("")
            continue

        # Round to 1 decimal place with half-up rounding
        # Use proper half-up rounding by adding small epsilon for values exactly at .05
        rounded_gpa = round(gpa + 1e-9, 1)

        # Determine letter grade based on rounded GPA
        if rounded_gpa == 4.0:
            letter = "A+"
        elif rounded_gpa >= 3.7:
            letter = "A"
        elif rounded_gpa >= 3.3:
            letter = "A-"
        elif rounded_gpa >= 3.0:
            letter = "B+"
        elif rounded_gpa >= 2.7:
            letter = "B"
        elif rounded_gpa >= 2.3:
            letter = "B-"
        elif rounded_gpa >= 2.0:
            letter = "C+"
        elif rounded_gpa >= 1.7:
            letter = "C"
        elif rounded_gpa >= 1.3:
            letter = "C-"
        elif rounded_gpa >= 1.0:
            letter = "D+"
        elif rounded_gpa >= 0.7:
            letter = "D"
        elif rounded_gpa > 0.0:
            letter = "D-"
        else:
            letter = "E"

        result.append(letter)

    return result