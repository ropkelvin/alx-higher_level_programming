#!/usr/bin/python3
'''
adds all arguments to a Python list,
and then save them to a file:
'''
import sys
import os

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file


def add_argv_to_list():
    """
    Returns a list of command line arguments.

    This function uses the sys module to get the command line arguments
    passed to the script, excluding the script name itself.

    Returns:
        A list of strings representing the command line arguments.
    """

    return sys.argv[1:]


if os.path.exists('add_item.json'):
    """
    Checks if the file 'add_item.json' exists in the current directory.

    If the file exists, it loads the JSON data from the file into the
    variable argv_list. If the file does not exist, argv_list is set
    to an empty list.
    """

    argv_list = load_from_json_file('add_item.json')
else:
    argv_list = []

"""
Appends the command line arguments to the existing list argv_list.

The command line arguments are obtained by calling the function
add_argv_to_list(). The extend() method is used to append the arguments
to argv_list.
"""
argv_list.extend(add_argv_to_list())

"""
Saves the updated argv_list to the file 'add_item.json'.

The function save_to_json_file() is called with argv_list and the filename
'add_item.json' as arguments. This writes the updated argv_list to the file
in JSON format.
"""
save_to_json_file(argv_list, 'add_item.json')
