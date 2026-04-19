def fruit_distribution(s: str, n: int) -> int:
    """
    Return the number of mango fruits in the basket.
    s: string describing number of apples and oranges.
    n: total number of fruits in the basket.
    """
    import re
    
    # Find all numbers in the string
    numbers = re.findall(r'\d+', s)
    
    # Convert to integers and sum
    total_apples_oranges = sum(int(num) for num in numbers)
    
    # Calculate mango count
    return n - total_apples_oranges