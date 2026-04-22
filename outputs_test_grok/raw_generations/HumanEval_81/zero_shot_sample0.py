from typing import List

def numerical_letter_grade(grades: List[float]) -> List[str]:
    def get_letter(g: float) -> str:
        if g > 4.0 + 1e-6 or g < 0.0 - 1e-6:
            return ''
        if g >= 4.0 - 1e-6:
            return 'A+'
        if g > 3.7 - 1e-6:
            return 'A'
        if g > 3.3 - 1e-6:
            return 'A-'
        if g > 3.0 - 1e-6:
            return 'B+'
        if g > 2.7 - 1e-6:
            return 'B'
        if g > 2.3 - 1e-6:
            return 'B-'
        if g > 2.0 - 1e-6:
            return 'C+'
        if g > 1.7 - 1e-6:
            return 'C'
        if g > 1.3 - 1e-6:
            return 'C-'
        if g > 1.0 - 1e-6:
            return 'D+'
        if g > 0.7 - 1e-6:
            return 'D'
        if g > 0.0 - 1e-6:
            return 'D-'
        return 'E'

    result = []
    for gpa in grades:
        # Round to 1 decimal place, half up
        if isinstance(gpa, (int, float)):
            rounded = round(gpa * 10) / 10
            result.append(get_letter(rounded))
        else:
            result.append('')
    return result