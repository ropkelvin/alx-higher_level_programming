#!/usr/bin/python3
'''Defines a rectangle class'''
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle shape, inheriting from the Base class.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle's position.
        __y (int): The y-coordinate of the rectangle's position.
        id (int): An identifier for the rectangle object.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
                                Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
                                Defaults to 0.
            id (int, optional): An identifier for the rectangle object.
                                Defaults to None.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
