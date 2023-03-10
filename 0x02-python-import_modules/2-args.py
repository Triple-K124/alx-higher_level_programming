#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""

import sys

args = sys.argv[1:]
num_args = len(args)

if num_args == 0:
    print("Number of argument(s): 0.")
    print(".")
else:
    print("Number of argument(s): {}.".format(num_args))
    print("Arguments:")
    for i, arg in enumerate(args):
        print("{}: {}".format(i+1, arg))
