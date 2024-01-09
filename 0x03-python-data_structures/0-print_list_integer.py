#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints each integer in a list on a seperate line without importing modules or casting an integer"""
    for num in my_list:
        print("{:d}".format(num))
