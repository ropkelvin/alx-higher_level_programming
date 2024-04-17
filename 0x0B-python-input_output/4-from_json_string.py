#!/usr/bin/python3
'''
function that returns an object (Python data structure)
represented by a JSON string:
'''
import json


def from_json_string(my_str):
    """
    Converts a JSON string into a Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        The Python object representation of the JSON string.
    """

    return json.loads(my_str)
