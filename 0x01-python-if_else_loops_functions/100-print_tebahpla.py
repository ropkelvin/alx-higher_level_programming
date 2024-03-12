#!/usr/bin/python3
for r in range(122, 96, -1):
    if r % 2 == 0:
        print("{:c}".format(r), end="")
    else:
        print("{:c}".format(r - 32), end="")
