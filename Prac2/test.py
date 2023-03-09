

def factorial_recursion(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursion(n-1)

def fibonacci_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

def number_base_conversion(n, b):
    """
    Number base conversion
    args:
        n - number to be converted
        b - base to convert to
    returns:
        n - converted number
    """
    if n == 0:
        return 0
    else:
        return n % b + 10 * number_base_conversion(n // b, b)

