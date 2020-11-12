#!/usr/bin/env python3

"""
Copyright 2020, University of Freiburg
Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

Usage of the Script:


"""
# stable_modells.py, written on: Donnerstag,  12 Oktober 2020.

import sys
from helping_stable import *

# Make sure that the main() Function of the DIMACS-Parser is imported and can be used
sys.path.insert(1, '../Exercise_01_01/')
from parser import main as dimacs


current = 0


def incCur():
    global current
    current += 1

def addCur(i : int):
    global current
    current += i

def resCur():
    global current
    current = 0


def get_impl_top(prog : str):
    for c in "TOP":
        if prog[current] != c:
            return ("-1", "-1")
        incCur()

    # If TOP is spelled correctly, set that the head has been found and skip the remaining two chars ", "
    addCur(2)
    running = True
    body = "TOP"
    head = ""

    while running and current < len(prog):
        char = prog[current]

        if char == ")":
            running = False
            break
            
        incCur()
        head += char

    return (body, head)


def get_impl(prog : str):
    
    # Check if the Word is spelled correctly
    for c in "Impl(":
        if prog[current] != c:
            return ("-1", "-1")
        incCur()

    running = True
    bracket_count = 1
    head = ""
    body = ""

    # Check if the current char is a "T", then it should be a Fact
    if prog[current] == "T":
        return get_impl_top(prog)


    # It makesk no difference if there is a BOT or a normal atom
    # Loop trough the whole prog and count the Brackets
    while running and current < len(prog):
        char = prog[current]

        # Count up if there is a "(" and count down when there is a ")"
        if char == "(":
            bracket_count += 1
        elif char == ")":
            bracket_count -= 1


        # If the bracket_count == 0 then the current char is ")" and the following should be a ","
        if bracket_count == 0:
            running = False
        else:
            incCur()

        body += char


    for i in range(len(body)-2, 0, -1):  # -2 becaus the ")" is irrelevant
        char = body[i]

        # Get the right head and do some syntax checking
        if char == " ":

            if body[i-1] != ",":

                print("Syntax Error! To may spaces between ',' and space or there is a space in the atom.")
                sys.exit(1)

            body = body[:i-1]  # -1 because the "," is irrelevant for the head
            break

        if char == ",":
            print("Syntax Error! You forgot the space between an atom an the ','.")
            sys.exit(1)

        head += char  # add the current char to the head, note that it is reversed

    head = head[-1::-1]  # reverse back the head

    return (body, head)


def cmpl_parser(prog : str):
    resCur()

    # The following Part to extract all the Impls out of the given programm and order it
    # ----------------------------------------------------------------------------------
    acc_impls = []
    acc_impls_spez_written = []

    bodys_bot = []
    heads_top = []

    while current < len(prog):
       
        char = prog[current]

        # Get all the Impls out of the string and chekc if it contains a TOP or a BOT
        if char == "I":

            acc_body, acc_head = get_impl(prog)

            # To make it genarl val[0] -> body, val[1] -> head, as intended in the exercise
            val = (acc_body, acc_head)

            # Append the certain value to the corresponding list
            if acc_head == "BOT":
                acc_impls_spez_written.append("Impl(%s, BOT)" % val[0])
                bodys_bot.append(val[0])

            elif acc_body == "TOP":
                acc_impls_spez_written.append("Impl(TOP, %s)" % val[1])
                heads_top.append(val[1])

            else:
                acc_impls.append(val)

        elif char != " " and char != ",":
            print("Syntax Error! You used a other char than ',' or a space between Formulars.")
            sys.exit(1)


        incCur()


    # The following Part is for creating the difference betzween the bodys and the heads
    # ----------------------------------------------------------------------------------

    # Zip up the list and get all the bodys
    bodys_impl, heads_impl = zip(*acc_impls)

    # Get all the atoms which are related to the impl rules
    tmp_body_impl = get_body_atoms(bodys_impl)
    tmp_head_impl = get_head_atoms(heads_impl)

    # Get all the atoms which are realted to the BOT rules
    tmp_body_bot = get_body_atoms(bodys_bot)


    # In those list are all the heads and all the bodys from every rule
    tmp_body_impl.extend(tmp_body_bot)
    tmp_head_impl.extend(heads_top)

    diff_atoms = list(set(tmp_body_impl) - set(tmp_head_impl))

    
    # The following Part is for adding all the atoms which are not in any head of the rules
    # -------------------------------------------------------------------------------------
    res = acc_impls_spez_written  # Later, it is a list with all the 
    
    for atom in diff_atoms:
        res.append("BiImpl(%s, BOT)" % atom)  

    

    # The following Part is for creating all the needed BiImpl rules
    # --------------------------------------------------------------

    acc_impls.sort(key=lambda x : x[1])  # Sort the all the impls by the header

    next_or = 0
    acc = "BiImpl("
    count_brack = 0

    # Format the rules with the same head into the desired format
    for n, val in enumerate(acc_impls):

        # If this is true, then there has been two rules with the same head
        if next_or != 0:
            
            # If the n-1 and the current rule has the same head and it is at the end, just close everything up
            if next_or == len(acc_impls)-1:
                acc += ", " + val[0] + ")" * (count_brack+1) + ", " + val[1] + ")"
                res.append(acc)
            
            # If we are not at the end and need to append one more Or(), because the next rule has also the same head
            elif val[1] == acc_impls[n+1][1]:
                acc += ", Or(" + val[0]
                next_or = n+1
                count_brack += 1
            
            # If the next rule has not the same head, then close it up and prepare for new run           
            elif val[1] != acc_impls[n+1][1]:
                acc += ", " + val[0] + ")" * (count_brack+1) + ", " + val[1] + ")"
                next_or = 0
                count_brack = 0

                res.append(acc)

                acc = "BiImpl("

        # If there is a start of a rule which has successor rule with the same head
        elif n < len(acc_impls)-1 and val[1] == acc_impls[n+1][1]:
            acc += "Or(" + val[0]
            next_or = n+1


        # If the predecessor rule has not the same head and there is no successor rule with the same head
        elif next_or == 0:
            res.append("BiImpl(%s, %s)" % (val[0], val[1]))


    return res  # In this list is the complete cmpl. At first all the BOT and TOP Rules, then the missing atoms, then the BiImpl rules




def main(prog : str):

    # Here you will get a list of all the 
    cmpl_res = cmpl_parser(prog)

    for form in cmpl_res:
        dimacs(form)



# tester = "Impl(a, g), Impl(And(a, b), popopo), Impl(And(b, d), quer), Impl(And(b, And(a, e)), qur), Impl(And(a, t), qur), Impl(And(b, c), quer), Impl(And(h, c), quer), Impl(TOP, aasdf), Impl(qasd, BOT), Impl(qa, BOT), Impl(And(asdf, s), zz), Impl(And(b, And(a, b)), quer), Impl(And(asdf, s), zz), Impl(And(af, s), zz), Impl(And(asf, s), zz), Impl(And(s, And(adf, And(a, And(qw, And(asd, fa))))), zz)"

tester = "Impl(And(a, b), a), Impl(q, asdf), Impl(And(qwe, asdf), BOT)"

if __name__ == '__main__':
    main(tester)
