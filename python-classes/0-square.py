#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """Represents a square with a private size attribute"""

    def __init__(self, size):
        """Initialize the square with size (no type/value checks)"""
        self.__size = size
