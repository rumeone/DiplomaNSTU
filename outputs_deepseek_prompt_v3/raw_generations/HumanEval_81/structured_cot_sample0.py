from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert numerical GPAs to letter grades according to the specified grading scale.
    
    The GPA is first rounded to one decimal place using half-up rounding,
    then converted to a letter grade using the provided table.
    For GPAs outside the valid range (0.0 to 4.0), an empty string is returned.
    
    Args:
        grades: List of float GPAs, each with one decimal place.
    
    Returns:
        List of corresponding letter grades.
    """
    def round_half_up(num: float) -> float:
        """Round to one decimal place using half-up method."""
        return round(num + 1e-6, 1)

    def gpa_to_letter(gpa: float) -> str:
        """Convert a single GPA to letter grade."""
        if not 0.0 <= gpa <= 4.0:
            return ''
        
        if gpa == 4.0:
            return 'A+'
        elif gpa > 3.7:
            return 'A'
        elif gpa > 3.3:
            return 'A-'
        elif gpa > 3.0:
            return 'B+'
        elif gpa > 2.7:
            return 'B'
        elif gpa > 2.3:
            return 'B-'
        elif gpa > 2.0:
            return 'C+'
        elif gpa > 1.7:
            return 'C'
        elif gpa > 1.3:
            return 'C-'
        elif gpa > 1.0:
            return 'D+'
        elif gpa > 0.7:
            return 'D'
        elif gpa > 0.0:
            return 'D-'
        else:  # gpa == 0.0
            return 'E'

    return [gpa_to_letter(round_half_up(g)) for g in grades]