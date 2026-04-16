#!/usr/bin/python3

#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that defines a square."""

    def __init__(self, size):
        """Initialize square with size."""
        self.__size = size

        if not  isinstance(self.__size, int):
            raise ValueError("size must be >= 0")
