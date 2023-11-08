#!/usr/bin/python3
""" Module contains function that returns True if the object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """Returns True or False if case i true of not"""
    return type(obj) == a_class
