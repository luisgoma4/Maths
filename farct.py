#write the factorial of a number
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
# Example usage ussing numpy
import numpy as np

def factorial_numpy(n):
    """Calculate factorial using numpy."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return np.math.factorial(n)