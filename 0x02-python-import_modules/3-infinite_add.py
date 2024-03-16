#!/usr/bin/python3

'''
    prints the result of the addition of all arguments
'''

import sys


def add_args():
    length = len(sys.argv)

    sum = 0
    for i in range(1, length):
        sum = sum + int(sys.argv[i])

    print("{}".format(sum))


if __name__ == "__main__":
    add_args()
