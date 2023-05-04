def fibonacci(n):
    """
    Return the nth value in the fibonacci series.
    
    Parameters:
    n (int): The index of the fibonacci number to be returned.

    Returns:
    int: The nth fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """
    Return the nth value in the lucas numbers.

    Parameters:
    n (int): The index of the lucas number to be returned.

    Returns:
    int: The nth lucas number.
    """
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, first=0, second=1):
    """
    Return the nth value in a series based on the provided first and second numbers.

    If first and second are not provided, the function returns the nth value in the fibonacci series.

    If first=2 and second=1, the function returns the nth value in the lucas numbers.

    Parameters:
    n (int): The index of the number to be returned.
    first (int, optional): The first number in the series. Defaults to 0.
    second (int, optional): The second number in the series. Defaults to 1.

    Returns:
    int: The nth number in the series.
    """
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)

if __name__ == "__main__":
    print(fibonacci(11))
    print(lucas(5))
    print(sum_series(7,0,1))