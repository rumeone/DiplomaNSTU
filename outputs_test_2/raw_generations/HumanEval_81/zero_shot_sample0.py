from typing import List

def numerical_letter_grade(grades: List[float]) -> List[str]:
    def round_half_up(n: float) -> float:
        if n < 0:
            return -round_half_up(-n)
        return int(n * 10 + 0.5) / 10

    result = []
    for g in grades:
        if g < 0 or g > 4.0:
            result.append('')
            continue
        
        rounded = round_half_up(g)
        
        if rounded >= 4.0 - 1e-6:
            grade = 'A+'
        elif rounded >= 3.7 - 1e-6:
            grade = 'A'
        elif rounded >= 3.3 - 1e-6:
            grade = 'A-'
        elif rounded >= 3.0 - 1e-6:
            grade = 'B+'
        elif rounded >= 2.7 - 1e-6:
            grade = 'B'
        elif rounded >= 2.3 - 1e-6:
            grade = 'B-'
        elif rounded >= 2.0 - 1e-6:
            grade = 'C+'
        elif rounded >= 1.7 - 1e-6:
            grade = 'C'
        elif rounded >= 1.3 - 1e-6:
            grade = 'C-'
        elif rounded >= 1.0 - 1e-6:
            grade = 'D+'
        elif rounded >= 0.7 - 1e-6:
            grade = 'D'
        elif rounded >= 0.0 - 1e-6:
            grade = 'D-'
        else:
            grade = 'E'
        
        result.append(grade)
    
    return result