#!/usr/bin/python3
"""Defines a base model class."""


class Base:
    """Represent the base model.

    Represents the "base" for all other classes in project 0x0C*.

    Attributes:
        __nb_objects (int): A private class variable
                            tracks the number of objects created.
        id (int): An identifier for the object.
                If not provided, it's automatically assigned.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int, optional): An identifier for the object.
                                If not provided, it's automatically assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
