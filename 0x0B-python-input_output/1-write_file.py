#!/usr/bin/python3
""" Module contains function that writes a string to a text file """


def write_file(filename="", text=""):
    """ Function that writes to a text file
    
    Args:
        filename: name of file to write to
        text: text to write

    Raises:
        Exception: Raises an exception if file cant be open or written

    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
