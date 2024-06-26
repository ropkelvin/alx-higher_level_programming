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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle, calculated as width * height.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints a rectangle of '#' characters at position (x, y).

        The dimensions of the rectangle are determined by:
        -the `self.__height` and `self.__width` attributes of the object.
        The rectangle is printed to the standard output,
        with each row of '#' characters printed on a new line.
        """
        print('\n' * self.y, end='')  # Add newlines for the y position
        for _ in range(self.height):
            print(' ' * self.x, end='')  # Add spaces for the x position
            print('#' * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: A string in the format
                "[Rectangle] (<id>) <x>/<y> - <width>/<height>".
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
               .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle object.

        Args:
            *args: A variable-length list of arguments.
            The order should be: id, width, height, x, y.
            **kwargs: A dictionary where each key represents
                    an attribute name and each value represents
                    the new value for that attribute.
        """
        attributes = ['id', 'width', 'height', 'x', 'y']

        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle object.

        Returns:
            dict: A dictionary that represents the Rectangle object,
            containing the following keys:
                - id
                - width
                - height
                - x
                - y
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
                }
