#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2-len(tuple_a))
    else:
        tuple_a = tuple_a[:2]
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2-len(tuple_b))
    else:
        tuple_b = tuple_b[:2]
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    list_c = [ ]
    for i in range(len(tuple_a)):
        list_c.append(list_a[i] + list_b[i])
    new_tuple = tuple(list_c)
    return new_tuple

