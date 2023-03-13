#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == " ":
        sentence[0] = None
    length = len(sentence)
    first = sentence[0]
    answer = (length, first)
    return(answer)
