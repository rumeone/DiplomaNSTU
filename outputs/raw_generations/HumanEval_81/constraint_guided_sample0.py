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
        rounded_gpa = round(gpa + 1e-9, 1)
        
        # Determine letter grade based on rounded GPA
        if rounded_gpa == 4.0:
            result.append('A+')
        elif rounded_gpa >= 3.7:
            result.append('A')
        elif rounded_gpa >= 3.3:
            result.append('A-')
        elif rounded_gpa >= 3.0:
            result.append('B+')
        elif rounded_gpa >= 2.7:
            result.append('B')
        elif rounded_gpa >= 2.3:
            result.append('B-')
        elif rounded_gpa >= 2.0:
            result.append('C+')
        elif rounded_gpa >= 1.7:
            result.append('C')
        elif rounded_gpa >= 1.3:
            result.append('C-')
        elif rounded_gpa >= 1.0:
            result.append('D+')
        elif rounded_gpa >= 0.7:
            result.append('D')
        elif rounded_gpa >= 0.0:
            result.append('D-')
        else:
            # This case should not occur due to bounds check, but included for completeness
            result.append('E')
    
    return result