#!/usr/bin/python3
'''
function that writes an Object to a text file,
using a JSON representation:
'''
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a file in JSON format.

    Args:
        my_obj: The Python object to be written to the file.
        filename (str): The name of the file to write to.
                        Defaults to an empty string.
    """
    import json
    with open(filename, mode='w', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
