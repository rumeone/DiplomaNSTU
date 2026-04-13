from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    if not numbers:
        return 0.0
    
    # Calculate mean
    mean_value = sum(numbers) / len(numbers)
    
    # Calculate sum of absolute differences from mean
    absolute_differences_sum = sum(abs(x - mean_value) for x in numbers)
    
    # Return average of absolute differences
    return absolute_differences_sum / len(numbers)