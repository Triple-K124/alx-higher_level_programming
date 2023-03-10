#!/usr/bin/python3

"""Import functions from calculator"""
from calculator_1 imiport add, sub, mul, div

if __name__ == "__main__":

    a = 10
    b = 5

    print("{} + {} = {}\n".format(a, b, (add(a, b))))
    print("{} - {} = {}\n".format(a, b, (sub(a, b))))
    print("{} * {} = {}\n".format(a, b, (mul(a, b))))
    print("{} / {} = {}".format(a, b, (div(a, b))))
