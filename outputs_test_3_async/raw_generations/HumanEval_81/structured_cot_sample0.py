from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert numerical GPAs to letter grades according to the specified grading scale.
    
    Args:
        grades: List of GPAs as floats (typically with one decimal place).
    
    Returns:
        List of letter grades corresponding to each GPA. For GPAs out of bounds,
        returns an empty string for that position.
    """
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
        # Round to 1 decimal place with half-up rounding
        rounded = round(gpa + 1e-9, 1)  # Add small epsilon for half-up
        
        # Check bounds
        if rounded < 0.0 or rounded > 4.0:
            result.append("")
            continue
        
        # Special case for exactly 0.0
        if abs(rounded - 0.0) < 1e-6:
            result.append("E")
            continue
        
        # Find appropriate letter grade
        letter_grade = ""
        for threshold, grade in grade_map:
            if rounded >= threshold:
                letter_grade = grade
                break
        
        result.append(letter_grade)
    
    return result