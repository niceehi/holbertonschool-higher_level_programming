#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with optional size."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size."""
        return self.__size

    @position.setter
    def position(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__position = value

    def area(self):
        """Return the square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using #."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
         
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__position[2]):
            print(" " * self.__position[0] + "#" * self.__size)
