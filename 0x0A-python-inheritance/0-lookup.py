#!/usr/bin/python3
"""
Function that returns a list of attributes and methods of the given object.

Parameters:
obj: Any object - The object for which need to be looked up.

Returns:
List - A list of strings representing the attributes and methods.
"""


def lookup(obj):
    """Returns the attribute and methods of an object"""
    return dir(obj)
