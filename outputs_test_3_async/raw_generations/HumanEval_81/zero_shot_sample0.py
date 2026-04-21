from typing import List


def numerical_letter_grade(grades: List[float]) -> List[str]:
    """
    It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of one decimal place GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E

    For input out of bounds, return an empty string.
    Also, the grade needs to be rounded (half up) to 1 decimal place if needed,
    before being converted to a letter grade. For edge scenarios, consider a tolerance of 1e-6.

    Example:
        grade_equation([4.0, 3, 1.72, 2, 3.5, 4.5]) ==> ['A+', 'B', 'C-', 'C', 'A-', '']
    """
    def round_half_up(n: float) -> float:
        if n < 0:
            return -round_half_up(-n)
        # Add a small epsilon to handle floating point precision issues
        epsilon = 1e-6
        n_adj = n + epsilon
        int_part = int(n_adj)
        frac_part = n_adj - int_part
        if frac_part >= 0.5:
            return (int_part + 1) / 1.0
        else:
            return int_part / 1.0

    result = []
    for grade in grades:
        # Round to 1 decimal place using half-up rounding
        rounded = round_half_up(grade * 10) / 10.0
        
        # Check bounds
        if rounded < 0.0 or rounded > 4.0:
            result.append('')
            continue
            
        # Apply tolerance for edge cases
        tolerance = 1e-6
        
        if abs(rounded - 4.0) <= tolerance:
            result.append('A+')
        elif rounded > 3.7 + tolerance:
            result.append('A')
        elif rounded > 3.3 + tolerance:
            result.append('A-')
        elif rounded > 3.0 + tolerance:
            result.append('B+')
        elif rounded > 2.7 + tolerance:
            result.append('B')
        elif rounded > 2.3 + tolerance:
            result.append('B-')
        elif rounded > 2.0 + tolerance:
            result.append('C+')
        elif rounded > 1.7 + tolerance:
            result.append('C')
        elif rounded > 1.3 + tolerance:
            result.append('C-')
        elif rounded > 1.0 + tolerance:
            result.append('D+')
        elif rounded > 0.7 + tolerance:
            result.append('D')
        elif rounded > 0.0 + tolerance:
            result.append('D-')
        else:
            result.append('E')
    
    return result