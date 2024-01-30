#!/usr/bin/python3
"""
This module defines `print_square`
The function prints a square
"""


def print_square(size):
    """prints a square with size, `size`
    Args:
        size (int)
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """

    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')

    for x in range(size):
        print('#' * size)

          if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/4-print_square.txt")
