#!/usr/bin/python3
""" Module defines a Rectangle Subclass square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Rectangle Subclass square """
    def __init__(self, size):
        """ Initialize a square.

        Args:
            size(int): The size of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
