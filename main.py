#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "Britt Bannister"


def add(x, y):
    """Add two integers."""
    return(x + y)


print(add(2, 4))


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    if(y == 0):
        return 0
    if(y > 0):
        return (add(x, multiply(x, y-1)))
    if (y < 0):
        return -multiply(x, -y)


print(multiply(6, -8))


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""

    return


def factorial(x):
    """Compute the factorial of x, where x > 0, using the functions above."""
    # your code here
    return


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    # your code here
    return


if __name__ == '__main__':
    # your code to call functions above
    pass
