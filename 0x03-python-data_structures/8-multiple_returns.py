#!/usr/bin/python3


def multiple_returns(sentence):
    """
    Returns tuple with the length of a string and its first
    character
    """
    s_leng = len(sentence)
    if s_leng == 0:
        f_char = None
    else:
        f_char = sentence[0]
    return ((s_leng, f_char))
