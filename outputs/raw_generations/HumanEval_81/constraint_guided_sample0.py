from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    Convert numerical GPAs to letter grades according to the specified scale.
    """
    result = []
    
    for gpa in grades:
        # Handle out of bounds
        if gpa < 0.0 or gpa > 4.0:
            result.append('')
            continue
            
        # Round to 1 decimal place with half-up rounding
        # Add small epsilon to handle floating point precision issues
        rounded = round(gpa + 1e-9, 1)
        
        # Determine letter grade based on thresholds
        if rounded >= 4.0 - 1e-6:
            letter = 'A+'
        elif rounded >= 3.7 - 1e-6:
            letter = 'A'
        elif rounded >= 3.3 - 1e-6:
            letter = 'A-'
        elif rounded >= 3.0 - 1e-6:
            letter = 'B+'
        elif rounded >= 2.7 - 1e-6:
            letter = 'B'
        elif rounded >= 2.3 - 1e-6:
            letter = 'B-'
        elif rounded >= 2.0 - 1e-6:
            letter = 'C+'
        elif rounded >= 1.7 - 1e-6:
            letter = 'C'
        elif rounded >= 1.3 - 1e-6:
            letter = 'C-'
        elif rounded >= 1.0 - 1e-6:
            letter = 'D+'
        elif rounded >= 0.7 - 1e-6:
            letter = 'D'
        elif rounded >= 0.0 - 1e-6:
            letter = 'D-'
        else:
            letter = 'E'
            
        result.append(letter)
    
    return result