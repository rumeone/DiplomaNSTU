from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    def round_half_up(n: float) -> float:
        if n < 0:
            return -round_half_up(-n)
        # Add a small epsilon to handle floating point precision issues
        eps = 1e-6
        int_part = int(n)
        frac_part = n - int_part
        if frac_part >= 0.5 - eps:
            return int_part + 1.0
        else:
            return float(int_part)

    result = []
    for grade in grades:
        if grade < 0.0 or grade > 4.0:
            result.append('')
            continue
        
        # Round to 1 decimal place using half-up
        rounded = round_half_up(grade * 10) / 10.0
        
        # Apply tolerance
        eps = 1e-6
        if abs(rounded - 4.0) < eps:
            result.append('A+')
        elif rounded > 3.7 - eps:
            result.append('A')
        elif rounded > 3.3 - eps:
            result.append('A-')
        elif rounded > 3.0 - eps:
            result.append('B+')
        elif rounded > 2.7 - eps:
            result.append('B')
        elif rounded > 2.3 - eps:
            result.append('B-')
        elif rounded > 2.0 - eps:
            result.append('C+')
        elif rounded > 1.7 - eps:
            result.append('C')
        elif rounded > 1.3 - eps:
            result.append('C-')
        elif rounded > 1.0 - eps:
            result.append('D+')
        elif rounded > 0.7 - eps:
            result.append('D')
        elif rounded > 0.0 - eps:
            result.append('D-')
        else:
            result.append('E')
    
    return result