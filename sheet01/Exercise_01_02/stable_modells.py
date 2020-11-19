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
    """
        This function is a helping function which gets the head atom of the Rule when its
        Body is a TOP. Then it is only needed to parse the remaining Atom in the head and 
        return it to the get_impl function.
    """

    for c in "TOP":
        if prog[current] != c:
            print_error("Syntax Error! You misspelled TOP.")
        incCur()

    # If TOP is spelled correctly, set that the head has been found and skip the remaining two chars ", "
    addCur(2)
    running = True
    body = "TOP"
    head = ""

    while running and current < len(prog):  # The len is that there is no endless loop
        char = prog[current]

        if char == ")":
            running = False
            break
            
        incCur()
        head += char

    # Basic Syntax checking. The head of this Rule should only contain chars
    for c in " (),":
        if c in head:
            print_error("Syntax Error! There is one of \" (),\" in the head of a TOP Rule.")

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
    inside = ""

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

        inside += char


    # Basic Syntax checking. The Syntax of Inside should be "BODY, ATOM)"
    if inside[-1] != ")": 
        print_error("Syntax Error! You forgot the last ) of the Rule.")
        sys.exit(1)


    for i in range(len(inside)-2, 0, -1):  # -2 becaus the ")" is irrelevant
        char = inside[i]

        # Get the right head and do some syntax checking
        if char == " ":

            if inside[i-1] != ",":

                print_error("Syntax Error! There is a invalid count of spaces at the Atom.")

            body = inside[:i-1]  # -1 because the "," is irrelevant for the head
            break

        if char == ",":
            print_error("Syntax Error! You forgot the space between an atom an the ','.")

        head += char  # add the current char to the head, note that it is reversed

    head = head[-1::-1]  # reverse back the head

    return (body, head)


def cmpl_parser(prog : str):
    """
        This function is used to parse a string which is a Program. So it contains only 
        Impl Rules. Those rules get parsed and all the needed Clark's Completion Rules
        get calculated and a List of all the full cmpl get returned.

        The Rules should be in the Following Syntax:

            "Impl(BODY, HEAD), Impl(BODY, HEAD), Impl(BODY, HEAD), ..."

        Therefore it is important that there are only commas and spaces between the rules
        otherewise it will throw a Syntax Error.

        This functions returns a Tuple. In the first element contains the whole cmpl and the
        second element contains all the Impl Rules which are needed to create the graph.
    """

    resCur()

    # The following Part to extract all the Impls out of the given programm and order it
    # ----------------------------------------------------------------------------------
    acc_impls = []  # List out of all values which needs to calculate the BiImpl Rules
    acc_impls_spez_written = []  # List of all TOP and BOT Rules which only gets printed

    bodys_bot = []  # If the Head of a Rule contains a BOT then the body Value get saved into this list
    heads_top = []  # When the Body contains a TOP then the Head is already the right atom

    # Parse trough the whole program
    while current < len(prog):
       
        char = prog[current]

        # Get all the Impls out of the string and chekc if it contains a TOP or a BOT
        if char == "I":

            acc_body, acc_head = get_impl(prog)

            # To make it genarl val[0] -> body, val[1] -> head, as intended in the exercise
            val = (acc_body, acc_head)

            # Append the certain value to the corresponding list
            if acc_head == "BOT":
                acc_impls_spez_written.append("BiImpl(%s, BOT)" % val[0])
                bodys_bot.append(val[0])

            elif acc_body == "TOP":
                acc_impls_spez_written.append("BiImpl(TOP, %s)" % val[1])
                heads_top.append(val[1])

            # If there is no BOT or TOP in the Rule, than it is a simple Impl() rule
            else:
                acc_impls.append(val)

        # You can use as many spaces and commas between the rules and it won't fail
        elif char != " " and char != ",":
            print_error("Syntax Error! You used a other char than ',' or a space between Rules.")


        incCur()


    # The following Part is for creating the difference betzween the bodys and the heads
    # ----------------------------------------------------------------------------------

    # Zip up the list and get all the bodys
    if len(acc_impls) > 0:
        bodys_impl, heads_impl = zip(*acc_impls)

        # Get all the atoms which are related to the impl rules
        tmp_body_impl = get_body_atoms(bodys_impl)
        tmp_head_impl = get_head_atoms(heads_impl)

    else:
        # Make sure to handle the case when there are no "normal" Rules in the provided Program
        tmp_body_impl = []
        tmp_head_impl = []


    # Get all the atoms which are realted to the BOT rules
    tmp_body_bot = get_body_atoms(bodys_bot)


    # In those list are all the heads and all the bodys from every rule
    tmp_body_impl.extend(tmp_body_bot)
    tmp_head_impl.extend(heads_top)

    # Remove all the duplicates from the lists so we can work with them later on
    tmp_body_impl = remove_duplicates(tmp_body_impl)
    tmp_head_impl = remove_duplicates(tmp_head_impl)


    # Get all the atoms which are in the body, but not in the head of any rule
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


    return (res, acc_impls) # In this list is the complete cmpl. At first all the BOT and TOP Rules, then the missing atoms, then the BiImpl rules




def main(prog : str):

    # Here you will get a list of all the
    (cmpl_res, imp_rules) = cmpl_parser(prog)

    for form in cmpl_res:
        print(form)

    print("\n\n")

    # Create the Graph which is needed to detect the loops
    compute_graph(imp_rules)


# tester = "Impl(a, g), Impl(And(a, b), popopo), Impl(And(b, d), quer), Impl(And(b, And(a, e)), qur), Impl(And(a, t), qur), Impl(And(b, c), quer), Impl(And(h, c), quer), Impl(TOP, aasdf), Impl(qasd, BOT), Impl(qa, BOT), Impl(And(asdf, s), zz), Impl(And(b, And(a, b)), quer), Impl(And(asdf, s), zz), Impl(And(af, s), zz), Impl(And(asf, s), zz), Impl(And(s, And(adf, And(a, And(qw, And(asd, fa))))), zz)"

# tester = "Impl(And(ab, And(a, And(e, f))), ab), Impl(TOP, ab), Impl(And(a, And(ab, And(c, e))), f), Impl(And(e, f), e), Impl(And(x, And(y, z)), BOT), Impl(a, f), Impl(f, a)"

# tester = "Impl(And(a, b), c), Impl(And(a, c), b), Impl(And(c, b), a), Impl(g, c), Impl(a, g), Impl(And(f, h), z), Impl(z, h)"

# tester = "Impl(And(a, c), b), Impl(TOP, a)"

tester = "Impl(a, c), Impl(And(b, d), c), Impl(And(b, c), d), Impl(e, d), Impl(b, e), Impl(And(c, d), e)"

# NOTE: Whene there is a Not in the Body, the parser can't detect it yet

if __name__ == '__main__':
    main(tester)
