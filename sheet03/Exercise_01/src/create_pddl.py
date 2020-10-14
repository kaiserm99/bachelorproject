#!/usr/bin/env python3

"""
Copyright 2020, University of Freiburg
Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>
Usage of the Script:
    
    This script opend the File kami.txt parses it and prints an ouput which is a problem in pddl.
    Make sure to have a correct kami.txt file, otherwise the problem will just fail.
    For example use:

        python3 create_pddl.py > porblem.pddl

"""
# create_pddl.py, written on: Donnerstag,  13 Oktober 2020.

import sys

colors = ['R', 'G', 'B', 'Y']  # red, green, blue, yellow


def main():
    

    try:
        f = open(sys.argv[1],"r")

    except FileNotFoundError:
        print("Invalid file or file path! Exiting...")
        exit(1)
    
    content = f.readlines()
    vertical = []


    for line in content:
        acc = []

        for char in line:
            if char == '\n':
                break

            acc.append(char)

        vertical.append(acc)

    acc_one = []
    acc_two = []
    acc_color = []

    for y, line in enumerate(vertical):

        for x, char in enumerate(line):

            acc_one.append("tile%d%d " %(x, y))

    acc_one.append("- tile")


    max_y = len(vertical)
    for y, line in enumerate(reversed(vertical)):

        max_x = len(line)

        for x, char in enumerate(line):

            if char == "R":
                acc_two.append("(color_value tile%d%d red)" % (x, y))

                if "red " not in acc_color:
                    acc_color.append("red ")

            elif char == "G":
                acc_two.append("(color_value tile%d%d green)" % (x, y))

                if "green " not in acc_color:
                    acc_color.append("green ")
            elif char == "B":
                acc_two.append("(color_value tile%d%d blue)" % (x, y))

                if "blue " not in acc_color:
                    acc_color.append("blue ")
            elif char == "Y":
                acc_two.append("(color_value tile%d%d yellow)" % (x, y))

                if "yellow " not in acc_color:
                    acc_color.append("yellow ")

            if x + 1 < max_x:
                acc_two.append("(is_neighbour tile%d%d tile%d%d)" % (x, y, x+1, y))

            if x - 1 >= 0:
                acc_two.append("(is_neighbour tile%d%d tile%d%d)" % (x, y, x-1, y))

            if y + 1 < max_y:
                acc_two.append("(is_neighbour tile%d%d tile%d%d)" % (x, y, x, y+1))

            if y - 1 >= 0:
                acc_two.append("(is_neighbour tile%d%d tile%d%d)" % (x, y, x, y-1))


    print("""(define (problem kami-prob)
    (:domain kami-dom)

    (:objects
        %s
        %s- color
        true - bool)

    (:init
(= (total-cost) 0)
%s)

    (:goal (and (not (curr_color true))
                (or """ % ("".join(acc_one), "".join(acc_color), "\n".join(acc_two)), end="\n")

    for c in acc_color:
        print("                   (forall (?t - tile) (color_value ?t %s))" % (c[:-1]), end="\n")


    print("                )))\n")
    print("    (:metric minimize (total-cost))\n)")

    f.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(1)

    main()