#!/usr/bin/env python3

"""
Copyright 2020, University of Freiburg
Bachelor-project - Foundations of Artificial Intelligence

Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

Description:

Usage of the Script:
    python3 nsp_tester.py <.modell encoded file>

"""
# nsp_tester.py, written on: Donnerstag,  12 Oktober 2020.


import sys


ASDF = ['fridafo', 'fridaft', 'fridaso', 'fridast', 'fritzfo', 'fritzft', 'fritzso', 'fritzst', 'heinzfo', 'heinzft', 'heinzno', 'heinznt', 'heinzso', 'heinzst', 'irafo', 'iraft', 'iraso', 'irast', 'norano', 'norant', 'udofo', 'udoft', 'udono', 'udont', 'udoso', 'udost']

def main():

    try:
        f = open(sys.argv[1],"r")

    except FileNotFoundError:
        print("Invalid file or file path! Exiting...")
        exit(1)

    content = f.readlines()

    for i, line in enumerate(content[1:]):  # [1:] because the first line is SAT
        line = line.split(" ")

        acc_day_one = [[], [], []]  # 0 -> früh, 1 -> spät, 2 -> nacht
        acc_day_two = [[], [], []]
        for n, char in enumerate(line[:-1]):


            if char[0] != "-":
                shift_name = ASDF[int(char)-1]
                
                if shift_name[-1] == "o":

                    if shift_name[-2] == "f":
                        acc_day_one[0].append(shift_name)

                    elif shift_name[-2] == "s":
                        acc_day_one[1].append(shift_name)

                    elif shift_name[-2] == "n":
                        acc_day_one[2].append(shift_name)


                else:
                    if shift_name[-2] == "f":
                        acc_day_two[0].append(shift_name)

                    elif shift_name[-2] == "s":
                        acc_day_two[1].append(shift_name)

                    elif shift_name[-2] == "n":
                        acc_day_two[2].append(shift_name)


        # Print a nice Table with the corresponding shifts
        print("  {0:11s} {1:10s} ({2})".format("Tag 1:", "Tag 2:", i+1))
        print("-"*25)
        for shift in range(3):
            for person in range(2):
            	# [:-2] because the last two chars are just the shift designation
                print("| {0:9s} | {1:10s}|".format(acc_day_one[shift][person][:-2], acc_day_two[shift][person][:-2]))
            print("|{0:11s}|{0:11s}|".format("-"*11))

        print(" ".join(line[:-1]))
        print("\n")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 %s <.modell encoded file>" % sys.argv[0])
        sys.exit(1)

    main()