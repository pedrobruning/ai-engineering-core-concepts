def greeting(): 
    print("Hi there!")

def is_fibonacci(num):
    """
    Check if a number is a Fibonacci number.
    
    A number is a Fibonacci number if and only if one or both of
    (5*n^2 + 4) or (5*n^2 - 4) is a perfect square.
    
    Args:
        num (int): The number to check
        
    Returns:
        bool: True if the number is a Fibonacci number, False otherwise
    """
    if num < 0:
        return False
    
    # Special case for 0
    if num == 0:
        return True
        
    # Check if 5*n^2 + 4 is a perfect square
    check1 = 5 * (num ** 2) + 4
    sqrt1 = int(check1 ** 0.5)
    
    # Check if 5*n^2 - 4 is a perfect square
    check2 = 5 * (num ** 2) - 4
    sqrt2 = int(check2 ** 0.5)
    
    # If either check1 or check2 is a perfect square, then num is a Fibonacci number
    return (sqrt1 ** 2 == check1) or (sqrt2 ** 2 == check2)