"""Calculate Mean Absolute Deviation (MAD) for a list of numbers."""

from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of the dataset.

    Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset:
    MAD = average | x - x_mean |

    Args:
        numbers: List of floating-point numbers.

    Returns:
        The Mean Absolute Deviation as a float.

    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    if not numbers:
        return 0.0

    mean = sum(numbers) / len(numbers)
    absolute_deviations = [abs(num - mean) for num in numbers]
    return sum(absolute_deviations) / len(absolute_deviations)