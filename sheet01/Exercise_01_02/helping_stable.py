#!/usr/bin/env python3

"""
Copyright 2020, University of Freiburg
Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

Usage of the Script:


"""
# helping_atble.py, written on: Donnerstag,  12 Oktober 2020.

import sys
from tarjan import *


# Copied from StackOverflow (https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python)
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_body_atoms(lst : list) -> list:
    """
        This function is used to parse all the given bodys and return all the atoms which are
        inside the given formulars.
        Returns a list with all the atoms which are in the formular
    """
    acc_body_atoms = []
    
    for body in lst:
        i = 0
        acc_atom = ""

        # If there is no A at the first char then it is only one atom in the body
        if body[0] != "A":

            # Basic Syntax checking. The body should only contain chars after the prev check
            for c in " (),":
                if c in body:
                    print_error("Syntax Error! There is one of \" (),\" in a atom which is alone in the body.")

            acc_body_atoms.append(body)
            continue

        while i < len(body):
            char = body[i]  # get the current char

            # Check if there is a And. If so it is not needed, because we only want to parse the atoms
            if char == "A":
                for j in "nd(":
                    i += 1
                    if body[i] != j:
                        print_error("Syntax Error! You misspelled And in a body.")

                i += 1
                # Check if the following char after ( is a invalid char
                if body[i] in " ,()":
                    print_error("Syntax Error! There is a invalid char after the And expression.")


            # If there is a space, then the previous char MUST be a comma
            elif char == " ":

                if body[i-1] != ",":
                    print_error("Syntax Error! There are spaces between atoms in the body.")

                i += 1

            elif (char == "," or char == ")") and len(acc_atom) > 0 and ")" not in acc_atom:  # the len because all the atoms can already be inside, then a empty atom would get appended
                
                acc_body_atoms.append(acc_atom)  # Add all atoms and the duplicates get removed afterwards
            
                acc_atom = ""  # Restore everything so the next run can start
                i += 1

            # It is assumed, that every other char is a pice of the atom
            else:
                acc_atom += char
                i += 1

    return acc_body_atoms  # Return all the atoms. There ARE duplicates


def get_head_atoms(lst : list):
    acc_head_atoms = []

    for head in lst:
        acc_head_atoms.append(head)

    return acc_head_atoms



def compute_graph(imp_rules : list):
    
    if len(imp_rules) == 0:
        print("You provided no Rules which don't contain a TOP or a BOT so there is no need for Loop-Formulars")
        return []

    graph = {}  # Save the graph as a dict

    # Zip up the list and get all the bodys
    bodys_impl, heads_impl = zip(*imp_rules)

    # Use this method to get all the body atoms
    acc_bodys = get_body_atoms(bodys_impl)
    acc_heads = get_head_atoms(heads_impl)


    # Insert all the body atoms into the graph, because the are likly no head atom and wouldn't get inserted into the graph
    for atom in acc_bodys:
        graph[atom] = Knoten(atom, [])

    # Make sure to add all the head atoms too, because they can be in no body and so it will occure a IndexError
    for atom in acc_heads:
        graph[atom] = Knoten(atom, []) 

    # Insert all the edges the current head atom is connected to 
    for i in range(len(imp_rules)):

        head_atom = heads_impl[i]
        body_atoms = get_body_atoms([bodys_impl[i]])  # Get all the body atoms of the current rule

        graph[head_atom].add_edges(body_atoms)

    print(graph)
    tj(graph)


def print_error(msg : str):
    print(bcolors.FAIL + msg + bcolors.ENDC)
    sys.exit(1)


def remove_duplicates(x):
    return list(dict.fromkeys(x))

