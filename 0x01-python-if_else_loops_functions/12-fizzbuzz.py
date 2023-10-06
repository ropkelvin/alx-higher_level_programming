#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        a = i % 5 == 0
        b = i % 3 == 0
        d = a and b
        output = f"FizzBuzz" if d else f"Buzz" if a \
            else f"Fizz" if b else f"{i:d}"
        print(output, end=" ")
