#!/usr/bin/python3

def element_at(my_list, idx):
    """Returns the element at the given index in the list, or None if the index is out of range."""

    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
