#!/usr/bin/python3
'''
function that returns the JSON representation of an object (string)
'''
import json


def to_json_string(my_obj):
    """
    Converts a Python object into a JSON string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: The JSON string representation of the Python object.
    """

    return json.dumps(my_obj)
