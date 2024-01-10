#!/usr/bin/python3


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    scorer = [scored*weight for (scored, weight) in my_list]
    return sum(scorer) / sum([weight for (scored, weight) in my_list])
