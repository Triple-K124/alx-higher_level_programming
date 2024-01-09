#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for i in range(len(matrix)):
        sum_len = len(matrix[i])
        for m in range(sum_len):
            if m != sum_len - 1:
                endCh = ' '
            else:
                endCh = ' '
            print("{:d}".format(matrix[i][m]), end=endCh)
        print("")
