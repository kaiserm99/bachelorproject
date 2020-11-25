#!/usr/bin/env python3

"""
Copyright 2020, University of Freiburg
Bachelor-project - Foundations of Artificial Intelligence

Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

Description:
    This script represents the given graph of cities and their connection
    to each other. With the help of Linear Programming a valid path from
    Frankfurt to München is calculated and the used edges get printed out
    at the end of the calculation.
    This file is static and if you want to use another graph, then you have
    to change the full array, weights, ... .

Usage:
    python3 shortest_path.py

"""
# shortest_path.py, written on: Mittwoch, 7 Oktober 2020.


"""
s = 1
t = 10

min 85*x_1,2 + 217*x_1,3 + 173*x_1,5 + 80*x_2,6 + 186*x_3,7 + 103*x_3,8 +
    183*x_4,8 + 250*x_6,9 + 167*x_8,10 + 502*x_5,10 + 84*x_9,10

Alle Variablen größer gleich 0

i = {1, 2, 3, 4, 5, 6, 8, 9}
j = {2, 3, 5, 6, 7, 8, 9, 10}

i = 1:
(x_1,2 + x_1,3 + x_1,5) - (0) = 1

i = 2:
(x_2,6) + (x_1,2) = 0

i = 3:
(x_3,7 + x_3,8) + (x_1,3) = 0

i = 4:
(x_4,8) - (0) = 0

i = 5:
(x_5,10) - (x_1,5) = 0

i = 6:
(x_6,9) - (x_2,6) = 0

i = 7:
(0) - (x_3,7) = 0

i = 8:
(x_8,10) - (x_3,8 + x_4,8) = 0

i = 9:
(x_9,10) - (x_6,9) = 0

i = 10:
(0) - (x_5,10  + x_8,10 + x_9,10) = -1


WICHTIG: Die Kanten gehen auch wieder zurück, was heißt, dass man alles nochmal nur negiert dazu machen muss.
"""

from scipy.optimize import linprog

def main():
    c = [85, 217, 173, 80, 186, 103, 183, 250, 167, 502, 84, 85, 217, 173, 80, 186, 103, 183, 250, 167, 502, 84]


    A = [
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,   -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0],
            [-1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,   1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
            [0, -1, 0, 0, 1, 1, 0, 0, 0, 0, 0,   0, 1, 0, 0, -1, -1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,    0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
            [0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 0,   0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0],
            [0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0,   0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0,   0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, -1, -1, 0, 1, 0, 0,  0, 0, 0, 0, 0, 1, 1, 0, -1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1,   0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -1],
            [0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
    ]


    b = [1, 0, 0, 0, 0, 0, 0, 0, 0, -1]


    bounds = []
    for i in range(11 * 2):
        bounds.append((0, None))


    res = linprog(c, A_eq=A, b_eq=b, bounds=bounds, method='simplex')


    # Print the whole result of the Linear Optimization
    print(res, end="\n\n")

    acc = 1
    for edge, value in enumerate(res.x):
        if value == 1:
            print("%d. Edge: %d" % (acc, edge+1))  # Assumed that the counting of the Edges starts with 1
            acc += 1



if __name__ == '__main__':
    main()
