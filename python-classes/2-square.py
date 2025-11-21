#!/usr/bin/python3
"""This module defines a class Square with a private size attribute and validation."""
class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a square with optional size, with type and value checks."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
