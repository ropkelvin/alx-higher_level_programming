#!/usr/bin/python3
'''Defines a Square class'''

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square shape, inheriting from the Rectangle class.

    Attributes:
        size (int): The size of the square (width and height are equal).
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): An identifier for the square object.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
                                Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
                                Defaults to 0.
            id (int, optional): An identifier for the square object.
                                Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        int: The size of the square (width and height are equal).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A string in the format
                "[Square] (<id>) <x>/<y> - <size>".
        """
        return "[Square] ({}) {}/{} - {}"\
               .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square object.

        Args:
            *args: A variable-length list of arguments.
            The order of the arguments should be: id, size, x, y.
            **kwargs: A dictionary where each key
            represents an attribute name and
            each value represents the new value for that attribute.
        """
        attributes = ['id', 'size', 'x', 'y']

        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    if attributes[i] == 'size':
                        self.width = arg
                        self.height = arg
                    else:
                        setattr(self, attributes[i], arg)

        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.width = value
                    self.height = value
                elif key in attributes:
                    setattr(self, key, value)
