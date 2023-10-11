#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    list_keys = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            list_keys.append(i)
    for i in list_keys:
        a_dictionary.pop(i)
    return a_dictionary
