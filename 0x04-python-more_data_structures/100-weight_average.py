#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    n = 0
    i = 0

    for tup in my_list:
        n += tup[0] * tup[1]
        i += tup[1]

    return (n / i)
