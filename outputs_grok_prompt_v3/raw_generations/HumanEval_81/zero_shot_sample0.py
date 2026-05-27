from typing import List
import math

def numerical_letter_grade(grades: List[float]) -> List[str]:
    def round_half_up(n: float) -> float:
        return math.floor(n * 10 + 0.5) / 10

    def get_letter(g: float) -> str:
        if g > 4.0 + 1e-6 or g < 0.0 - 1e-6:
            return ''
        if abs(g - 4.0) < 1e-6:
            return 'A+'
        if g > 3.7:
            return 'A'
        if g > 3.3:
            return 'A-'
        if g > 3.0:
            return 'B+'
        if g > 2.7:
            return 'B'
        if g > 2.3:
            return 'B-'
        if g > 2.0:
            return 'C+'
        if g > 1.7:
            return 'C'
        if g > 1.3:
            return 'C-'
        if g > 1.0:
            return 'D+'
        if g > 0.7:
            return 'D'
        if g > 0.0:
            return 'D-'
        if abs(g - 0.0) < 1e-6:
            return 'E'
        return ''

    return [get_letter(round_half_up(g)) for g in grades]