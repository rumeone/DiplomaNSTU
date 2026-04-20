from typing import List

def numerical_letter_grade(grades: List[float]) -> List[str]:
    def round_half_up(n: float) -> float:
        if n < 0:
            return -round_half_up(-n)
        int_part = int(n)
        frac = n - int_part
        if frac >= 0.5:
            return int_part + 1
        return int_part + frac

    result = []
    for g in grades:
        if g < 0.0 or g > 4.0:
            result.append('')
            continue
        
        rounded = round_half_up(g * 10) / 10
        rounded = round(rounded, 1)
        
        if abs(rounded - 4.0) < 1e-6:
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