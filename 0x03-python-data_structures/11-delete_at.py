#!/usr/bin/python3


def delete_at(my_list=[], idx=0):

    l_leng = len(my_list)
    if idx >= l_leng or idx < 0:
        return (my_list)

    del my_list[idx]
    return (my_list)