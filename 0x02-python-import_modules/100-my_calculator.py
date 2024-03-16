#!/usr/bin/python3

'''
    imports all functions from the file calculator_1.py
    and handles basic operations.
'''

import sys
from calculator_1 import add, sub, mul, div


def calc():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if sys.argv[2] == '+':
            result = add(a, b)
        elif sys.argv[2] == '-':
            result = sub(a, b)
        elif sys.argv[2] == '*':
            result = mul(a, b)
        elif sys.argv[2] == '/':
            result = div(a, b)

        print("{} {} {} = {}".format(a, sys.argv[2], b, result))


if __name__ == "__main__":
    calc()
