def only_diff_elements(set_1, set_2):
    new_set = set_1 - set_2
    new_set_2 = set_2 - set_1
    total_set = new_set | new_set_2
    return total_set
