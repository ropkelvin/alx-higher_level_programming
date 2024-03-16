#!/usr/bin/python3

'''
    prints all the names defined by the compiled module
'''

import hidden_4


def names():
    for i in dir(hidden_4):
        if not i.startswith("__"):
            print("{}".format(i))


if __name__ == "__main__":
    names()
