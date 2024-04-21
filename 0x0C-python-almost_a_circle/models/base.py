#!/usr/bin/python3
"""Defines a base model class."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        If the input is None, it returns an empty JSON array string "[]".

        Args:
            list_dictionaries (list): A list of dictionaries to be converted.

        Returns:
            str: JSON string representation of the input list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherits from Base.
                    Example: list of Rectangle or list of Square instances.
        """

        if list_objs is None:
            list_objs = []

        list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)

        with open(cls.__name__ + ".json", 'w') as file:
            file.write(json_string)
