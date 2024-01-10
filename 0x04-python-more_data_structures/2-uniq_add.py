def uniq_add(my_list=[]):
    seen = set(my_list)
    a = 0
    for x in seen:
        a += x
    return a
