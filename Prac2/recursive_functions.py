def factorial_recursive(input):
    """
    Test input for:
        - positive (can be 0)
        - integer
    """
    if not type(input) is int:
        raise ValueError("Input must be integer")
    elif input < 0:
        raise ValueError("Input must be positive")
    else:
        return _factorial_recursive(input)


def _factorial_recursive(input):
    """
    fact(n) = 1             <- base class
    fact(n-1) = 2 * 1       <- f(n-1)
    face(n-2) = 3 * 2 * 1

    Requires:
        n to be positive integer
    """
    factorial = 1
    if input == 0:
        factorial == 1
    else:
        factorial = input * factorial_recursive(input - 1)
    return factorial


def fibonacci_recursive(n):
    """
    f(0) = 0                    <- base 1
    f(1) = 1                    <- base 2
    f(2) = 1  (f(1)+f(0))       <- first recursion
    f(3) = 2  (f(2)+f(1)+f(0))

    Requires:
        n to be positive integer
    """
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    return result


def common_denominator_recursive(a, b):
    """
    commmon denominator
    By hand example, for 12 and 9, the common denom is 3.
        12 / 9 = 1r3.  9 / 3 = 3   <- no remainder.
        27 / 6 = 4r3.  6 / 3 = 0   <- no remainder
        132 / 72 = 1r60.  72 / 60 = 1r12.  60 / 12 = 5

    if a / b != int, divide a by the remainder.  % in python gives remainder
    if a % b == 0, return a         <- base case
    else b % (a % b)                <- repeat

    Requires:
        a and b to be integers
    """
    result = 0
    if b == 0:
        result = a
    else:
        result = common_denominator_recursive(b, a % b)
    return result


def base_conversion_recursive(input, base):
    """
    1. Divide the decimal number by new base
    2. Remainder is lsb on number in new base
    3. Divide the result by the new base
    4. Remainder is next significant bit of new base (10 * current place)
    5. Repeat until answer is 1r0

    In python "%" operator gives the remainder and "//" is the floor division

    9(10) to (2):
        9/2 = 4r1
        4/2 = 2r0
        2/2 = 1r0
        0/2 = 0     <- stop condition when input becomes 0
    """
    result = 0
    remainder = input % base
    quotient = input // base
    if input == 0:
        result = input
    else:
        result = remainder + 10 * base_conversion_recursive(quotient, base)
    return result
