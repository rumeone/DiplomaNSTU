from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert a list of numerical GPAs to letter grades according to the specified grading scale.
    
    The GPAs are first rounded to one decimal place using half-up rounding,
    then mapped to letter grades. Invalid GPAs return an empty string.
    """
    def round_half_up(x: float) -> float:
        """Round to one decimal place using half-up rounding."""
        return round(x + 1e-9, 1)  # Add small epsilon to handle floating-point precision
    
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
        (-float('inf'), "E")
    ]
    
    result = []
    for gpa in grades:
        if gpa < 0.0 or gpa > 4.0:
            result.append("")
            continue
        
        rounded = round_half_up(gpa)
        
        for threshold, letter in grade_map:
            if rounded >= threshold:
                result.append(letter)
                break
    
    return result