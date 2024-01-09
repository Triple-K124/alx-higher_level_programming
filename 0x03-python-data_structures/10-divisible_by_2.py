#!/usr/bin/python3


def divisible_by_2(my_list=[]):

    list_leng = len(my_list)
    if list_leng == 0:
        return None

    bool_listy = []
    for i in range(list_leng):
        if my_list[i] % 2 == 0:
            bool_listy.append(True)
        else:
            bool_listy.append(False)
    return (bool_listy)
