#!/usr/bin/python3
""" Module that contains class BaseGeometry """


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        """ Public instance method that raises and exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates a parameter as an integer
        Args:
            name(str): name of the parameter
            value(int): parameter to validate
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
