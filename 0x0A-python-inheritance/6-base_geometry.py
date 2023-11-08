#!/usr/bin/python3
""" class BaseGeometry (based on 5-base_geometry.py) """


class BaseGeometry:
    """ Public instance method that raises and exception """
    def area(self):
        raise Exception("area() is not implemented")
