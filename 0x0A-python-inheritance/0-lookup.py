#!/usr/bin/python3


def lookup(obj):
    """
    Function that returns a list of attributes and methods of the given object.

    Parameters:
    obj: Any object - The object for which need to be looked up.

    Returns:
    List - A list of strings representing the attributes and methods.
    """
    return dir(obj)
