#!/usr/bin/python3

def no_c(my_string):
    """Removes all lowercase and uppercase 'c' characters from a string."""

    new_string = " " # Create an empty string to store the modified result
    for i in my_string:
        if i not in "Cc": # Check if the character is not 'c' or 'C'
            new_string += i # Add it to the new string
    return new_string # Return the string without 'c' characters
