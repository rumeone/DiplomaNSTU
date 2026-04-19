from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    result = []
    for g in grades:
        # Round to 1 decimal place with half-up rounding
        # Add small epsilon to handle floating point issues
        rounded = round(g + 1e-9, 1)
        
        # Check bounds
        if rounded < 0.0 or rounded > 4.0:
            result.append('')
            continue
            
        if rounded == 4.0:
            result.append('A+')
        elif rounded > 3.7:
            result.append('A')
        elif rounded > 3.3:
            result.append('A-')
        elif rounded > 3.0:
            result.append('B+')
        elif rounded > 2.7:
            result.append('B')
        elif rounded > 2.3:
            result.append('B-')
        elif rounded > 2.0:
            result.append('C+')
        elif rounded > 1.7:
            result.append('C')
        elif rounded > 1.3:
            result.append('C-')
        elif rounded > 1.0:
            result.append('D+')
        elif rounded > 0.7:
            result.append('D')
        elif rounded > 0.0:
            result.append('D-')
        else:
            result.append('E')
    
    return result