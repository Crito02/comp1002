from recursive_functions import factorial_recursive,\
                                fibonacci_recursive,\
                                common_denominator_recursive,\
                                base_conversion_recursive


def test_factorial_recursive():
    assert factorial_recursive(0) == 1
    assert factorial_recursive(1) == 1
    assert factorial_recursive(2) == 2
    assert factorial_recursive(4) == 24
    print("Factorial tests passed")


def test_fibonacci_recursive():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(9) == 34
    print("Fibonacci tests passed")


def test_common_denominator_recursive():
    assert common_denominator_recursive(12, 9) == 3
    assert common_denominator_recursive(27, 6) == 3
    assert common_denominator_recursive(132, 72) == 12
    print("GCD tests passed")


def test_base_conversion_recursive():
    assert base_conversion_recursive(8, 16) == 8
    assert base_conversion_recursive(792, 16) == 318
    assert base_conversion_recursive(37, 2) == 100101


if __name__ == '__main__':
    test_factorial_recursive()
    test_fibonacci_recursive()
    test_common_denominator_recursive()
    test_base_conversion_recursive()
