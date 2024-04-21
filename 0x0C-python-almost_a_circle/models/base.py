#!/usr/bin/python3
"""Defines a base model class."""
import json
import csv
import turtle
import random


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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by the JSON string json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: If json_string is None or empty, return an empty list.
                Otherwise, return the list represented by json_string.
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: A dictionary where each key represents an
            attribute name
            and each value represents the new value for that attribute.

        Returns:
            An instance of the class that called this method,
            with its attributes set to the values provided in the dictionary.
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.

        The filename must be: <Class name>.json - example: Rectangle.json
        If the file does not exist, return an empty list
        Otherwise, return a list of instances
        -the type of these instances depends on cls
                    (current class using this method)

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                list_dicts = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []

        return [cls.create(**dict_) for dict_ in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes the CSV string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherits from Base.
                    Example: list of Rectangle or list of Square instances.
        """
        filename = cls.__name__ + ".csv"

        with open(filename, 'w', newline='') as csvfile:
            if list_objs is not None:
                writer = csv.writer(csvfile)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances from a CSV file.

        The filename must be: <Class name>.csv - example: Rectangle.csv
        If the file does not exist, return an empty list
        Otherwise, return a list of instances
        -the type of these instances depends on cls
                    (current class using this method)

        Returns:
            list: A list of instances.
        """
        filename = cls.__name__ + ".csv"
        list_objs = []

        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(row[0]), "width": int(row[1]),
                                      "height": int(row[2]),
                                      "x": int(row[3]), "y": int(row[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(row[0]), "size": int(row[1]),
                                      "x": int(row[2]), "y": int(row[3])}
                    list_objs.append(cls.create(**dictionary))
        except FileNotFoundError:
            pass

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles (list): A list of Rectangle instances.
            list_squares (list): A list of Square instances.
        """
        screen = turtle.Screen()
        screen.bgcolor("black")

        t = turtle.Turtle()

        colors = ["red", "green", "blue", "orange", "purple",
                  "brown", "yellow"]

        for rectangle in list_rectangles:
            t.penup()
            t.goto(rectangle.x, rectangle.y)
            t.pendown()
            t.color(random.choice(colors))
            for _ in range(2):
                t.forward(rectangle.width)
                t.right(90)
                t.forward(rectangle.height)
                t.right(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.color(random.choice(colors))
            for _ in range(4):
                t.forward(square.size)
                t.right(90)

        t.hideturtle()
        turtle.done()
