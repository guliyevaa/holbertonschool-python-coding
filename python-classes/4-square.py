#!/usr/bin/python3
"""Define a Square class with printing capability"""


class Square:
    """Represents a square with a private size attribute"""

    def __init__(self, size=0):
        """Initialize the square with optional size"""
        self.size = size  # Use setter for validation

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
