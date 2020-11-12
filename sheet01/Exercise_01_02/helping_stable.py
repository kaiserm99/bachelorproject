#!/usr/bin/env python3

"""
Copyright 2020, University of Freiburg
Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

Usage of the Script:


"""
# helping_atble.py, written on: Donnerstag,  12 Oktober 2020.


def get_body_atoms(lst : list):
    acc_body_atoms = []
    
    for rule in lst:
        i = 0
        acc_atom = ""

        if rule[0] != "A":
            acc_body_atoms.append(rule)
            continue

        while i < len(rule):
            char = rule[i]  # get the current char

            if char == "A":
                i += 4

            elif char == " ":
                i += 1

            elif (char == "," or char == ")") and len(acc_atom) > 0 and ")" not in acc_atom:  # the len because all the atoms can already be inside, then a empty atom would get appended
                
                if acc_atom not in acc_body_atoms:  # if the atom is already inside, don't append
                    acc_body_atoms.append(acc_atom)
            
                acc_atom = ""  # Restore everything so the next run can start
                i += 1

            else:
                acc_atom += char
                i += 1

    return acc_body_atoms


def get_head_atoms(lst : list):
    acc_head_atoms = []

    for head in lst:
        acc_head_atoms.append(head)

    return acc_head_atoms