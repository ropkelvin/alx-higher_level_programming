#!/usr/bin/python3

'''
    prints all integers of a list, in reverse order.
'''


def print_reversed_list_integer(my_list=[]):
    i = (len(my_list) - 1)
    for j in range(i, -1, -1):
        print("{:d}".format(my_list[j]))
