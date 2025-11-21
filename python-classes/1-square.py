#!/usr/bin/python3
"""This module defines a class Square with a private size attribute and validation.
"""

class Square:
    """Defines a square with a private size attribute."""

    def __init__(self, size=0):
        """Initialize a square with optional size, with type and value checks."""
        # Type validation
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Value validation
        if size < 0:
            raise ValueError("size must be >= 0")
        # Private attribute
        self.__size = size
