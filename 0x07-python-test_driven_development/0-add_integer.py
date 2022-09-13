#!/usr/bin/python3
"""
function that adds two integers
"""


def add_integer(a, b=98):
    """
    this function returns the sum of two numbers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a is None:
        raise TypeError("'NoneType' object is not subscriptable")
    if b is None:
        raise TypeError("'NoneType' object is not subscriptable")

    return int(a) + int(b)
