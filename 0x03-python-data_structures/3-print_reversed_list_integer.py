#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    "Prints the integers of a list in reversed order, one per line."""

    my_list.reverse()  # Reverse the list in place
    for rev in my_list:
        print("{:d}".format(rev)) #Print each reversed integer
 
