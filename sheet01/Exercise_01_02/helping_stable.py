#!/usr/bin/env python3

"""
Copyright 2020, University of Freiburg
Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

Usage of the Script:


"""
# helping_stable.py, written on: Donnerstag,  12 Oktober 2020.

import sys
import networkx as nx
import matplotlib.pyplot as plt


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
        inside the given formulas.
        Returns a list with all the atoms which are in the formula
    """
    acc_body_atoms = []
    
    for body in lst:
        i = 0
        acc_atom = ""

        # Make sure to handle the Nots when they are alone in the body of a rule
        if body[0] == "N":

            for j in "ot(":
                i += 1
                if body[i] != j:
                    print_error("Syntax Error! You misspelled Not in a body.")

            i += 1  # The pointer points now on the first digit of the atom and the las char is a )
            
            # Last char should be a )
            if body[-1] != ")":
                print_error("Syntax Error! You forgot to close a Not.")
            

            body = "-" + body[i:-1]  # The not and the ) gets removed, make sure to add the -

            # Check if it contains a invalid char
            for c in " (),":
                if c in body:
                    print_error("Syntax Error! There is one of \" (),\" in a atom which is alone in the body.")
            
            acc_body_atoms.append(body)
            continue


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

            elif char == "N":
                for j in "ot(":
                    i += 1
                    if body[i] != j:
                        print_error("Syntax Error! You misspelled Not in a body.")

                i += 1
                # Check if the following char after ( is a invalid char
                if body[i] in " ,()":
                    print_error("Syntax Error! There is a invalid char after a Not expression.")

                acc_atom = "-"

            # It is assumed, that every other char is a pice of the atom
            else:
                acc_atom += char
                i += 1

    # print(acc_body_atoms)
    return acc_body_atoms  # Return all the atoms. There ARE duplicates


def get_head_atoms(lst : list):
    acc_head_atoms = []

    for head in lst:
        acc_head_atoms.append(head)

    return acc_head_atoms



def compute_loops(imp_rules : list):
    
    if len(imp_rules) == 0:
        print("You provided no Rules which don't contain a TOP or a BOT so there is no need for Loop-Formulas")
        return []

    graph = {}  # Save the graph as a dict

    # Zip up the list and get all the bodys
    bodys_impl, heads_impl = zip(*imp_rules)

    # Use this method to get all the body atoms
    acc_bodys = get_body_atoms(bodys_impl)
    acc_heads = get_head_atoms(heads_impl)


    # Insert all the body atoms into the graph, because the are likly no head atom and wouldn't get inserted into the graph
    for atom in acc_bodys:
        if atom[0] != "-":
            graph[atom] = []

    # Make sure to add all the head atoms too, because they can be in no body and so it will occure a IndexError
    for atom in acc_heads:
        graph[atom] = []

    # Insert all the edges the current head atom is connected to 
    for i in range(len(imp_rules)):

        head_atom = heads_impl[i]
        body_atoms = get_body_atoms([bodys_impl[i]])  # Get all the body atoms of the current rule

        for vert in body_atoms:

            # NOTE: Check if a sling to the same atom is valid

            # Check if the current Vertex is a not atom. If so don't add a edge
            if vert[0] != "-" and vert != head_atom:
                # There is no need for a test if the edge is already in the graph or not
                graph[vert].append(head_atom)

    # print(graph)
    # At this point the Graph is fully formed and we need to calculate all the Loops by using networkx
    graph = nx.DiGraph(graph)
 
    # draw_graph(graph)
    loops = list(nx.simple_cycles(graph))  # This is a list of lists with all the loops in the graph

    return loops


def compute_loop_formula(loops : list, imp_rules : list):

    loop_formulas = []

    # Loop through all loops and create R-
    for loop in loops:

        r_minus = {}

        for atom in loop:

            # Check if the atom is already in the dict, when not create a entry
            if atom not in r_minus:
                r_minus[atom] = []


            i = 0

            found = False
            while i < len(imp_rules):

                rule = imp_rules[i]

                # If the head of the current rule is matching with the atom out of the current loop
                if rule[1] == atom:
                    found = True

                    body_atoms = get_body_atoms([rule[0]])

                    # Check if the body atoms of the current rule are in the current loop
                    append = True
                    for ba in body_atoms:
                
                        # NOTE: Unsure what to do when there is a neg atom in the body_atoms, which is positiv in the loop

                        if ba in loop:
                            append = False
                            break

                    # If there was no atom in the body of the rule, which is also in the current loop. Append it
                    if append:
                        # Check if this Body is already in the dict. If so, just skip
                        if rule[0] not in r_minus[atom]:
                            r_minus[atom].append(rule[0])


                # imp_rules is sorted by the head of the rule. So if we have found one matching atom with a head
                # and the next one is not matching, then there are no more rules with a matching head
                elif rule[1] != atom and found:
                    break

                # Count to the next atom 
                i += 1

        # r_minus is now a dict with all the p Atoms and all the corresponding Bodys.
        # Now apply the last Loop-Formula rule

        all_bodys = []
        all_heads = []

        for head, bodys in r_minus.items():

            # There is no need to check for dupplicates beacause the Loop-Formula has a Or in it
            for body in bodys:
                all_bodys.append(body)
            all_heads.append(head)


        # Bring all the Bodys in the right form: Not(Or(Body, Or(Body, ...)))
        left = write_rules(all_bodys, "Or", wrapper_op="Not")

        # Bring all the Heady in the right form: And(Not(p1), And(Not(p2), ...))
        right = write_rules(all_heads, "And", atom_start="Not(", atom_end=")")

        loop_formulas.append("Impl({0}, {1})".format(left, right))

    # Return the resulting Loop-Formulas
    return loop_formulas


def write_rules(lst : list, op, atom_start="", atom_end="", wrapper_op=""):
    count = len(lst)
    written = ""

    if wrapper_op != "":
        written += wrapper_op + "("

    if count == 0:
        written += "BOT" 

    elif count == 1:
        written += "{1}{0}{2}".format(lst[0], atom_start, atom_end)

    elif count == 2:
        written += "{0}({3}{1}{4}, {3}{2}{4})".format(op, lst[0], lst[1], atom_start, atom_end)

    else:

        written += "{0}({2}{1}{3}".format(op, lst[0], atom_start, atom_end)

        bracket_count = 0
        for n, body in enumerate(lst[1:]):

            if count - n == 3:
                written += ", {0}({3}{1}{4}, {3}{2}{4}{5}".format(op, lst[-2], lst[-1], atom_start, atom_end, ")" * (bracket_count+2))
                break

            written += ", {0}({2}{1}{3}".format(op, body, atom_start, atom_end)
            bracket_count += 1

    if wrapper_op != "":
        written += ")"

    return written


def print_error(msg : str):
    print(bcolors.FAIL + msg + bcolors.ENDC)
    sys.exit(1)


def remove_duplicates(x):
    return list(dict.fromkeys(x))


def remove_nots(lst : list) -> list:
    for n, atom in enumerate(lst):
        if atom[0] == "-":
            lst[n] = atom[1:]
    return lst


def draw_graph(graph : nx.DiGraph):
    nx.draw_networkx(graph)
    plt.show()

