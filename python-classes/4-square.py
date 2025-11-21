#!/usr/bin/python3
"""Defines a square class with printing capability"""

class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize the square with optional size"""
        self.size = size

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with type and value checks"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' character"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
