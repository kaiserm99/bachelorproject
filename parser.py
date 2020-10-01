#!/usr/bin/env python3

"""
Copyright 2020, University of Freiburg
Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

Usage of the Script:


"""
# parser.py, written on: Donnerstag,  1 Oktober 2020.


import string

class Formular:
    def __init__(self, value = "init", left = "-", right = "-", neg = "-"):
        self.value = value
        self.left = left
        self.right = right
        self.neg = neg

    def __str__(self):
        
        if self.value == "Not":
            acc = "\u00AC " + str(self.neg)
            
        elif self.value in string.ascii_lowercase and len(self.value) == 1:
            acc = self.value
            
        elif self.value == "And":
            acc = "(" + str(self.left) + " \u2227 " + str(self.right) + ")"

        elif self.value == "Or":
            acc = "(" + str(self.left) + " \u2228 " + str(self.right) + ")"

        else:
            acc = self.value + "(" + str(self.left) + " | " + str(self.right) + ")"
        
        return acc



current = 0


def incCur():
    global current
    current += 1


def parseOr(formular : Formular) -> Formular:

    # Check if the Word is spelled correctly
    for c in "r(":
        if formular[current] != c:
            return False
        incCur()
        
    left = parseFormular(formular)
    
    
    right = parseFormular(formular)

    if left is False or right is False:
        return False

    return Formular("Or", left, right)


def parseAnd(formular : Formular) -> Formular:

    # Check if the Word is spelled correctly
    for c in "nd(":
        if formular[current] != c:
            return False
        incCur()
        
    left = parseFormular(formular)
    
    
    right = parseFormular(formular)

    if left is False or right is False:
        return False

    return Formular("And", left, right)


# A -> B --> -A o B
def parseImpl(formular : Formular) -> Formular:

    # Check if the Word is spelled correctly
    for c in "mpl(":
        if formular[current] != c:
            return False
        incCur()
        
    left = parseFormular(formular)
    
    
    right = parseFormular(formular)

    if left is False or right is False:
        return False

    return Formular("Or", Formular("Not", neg=left), right)



# A <-> B --> (-A o B) u () (A o -B)
def parseBiImpl(formular : Formular) -> Formular:

    # Check if the Word is spelled correctly
    for c in "iImpl(":
        if formular[current] != c:
            return False
        incCur()
        
    left = parseFormular(formular)
    
    
    right = parseFormular(formular)

    if left is False or right is False:
        return False

    return Formular("And",
                    Formular("Or", 
                        Formular("Not", neg=left),
                        right), 
                    Formular("Or",
                        left,
                        Formular("Not", neg=right)))



def parseNot(formular : Formular) -> Formular:

    # Check if the Word is spelled correctly
    for c in "ot(":
        if formular[current] != c:
            return False
        incCur()
        
    value = parseFormular(formular)

    if value is False:
        return False

    return Formular("Not", neg = value)



def parseAtom(formular) -> Formular:

    return Formular(formular[current - 1])



def parseFormular(formular : str, acc = Formular) -> Formular:
    """ 
        This function is used to parse the whole formular which is given by an string.
        The global Variable current takes care of which letter is used at the moment.
        This function takes care of the Implications and the Äquvalations and replaces
        it directly.

        Doctests:
            >>> acc = parseFormular("And(Impl(Not(a), And(BiImpl(a, b), b)), And(Not(b), Not(a)))")
            >>> print(acc)
            ((¬ ¬ a ∨ (((¬ a ∨ b) ∧ (a ∨ ¬ b)) ∧ b)) ∧ (¬ b ∧ ¬ a))
    """
    if len(formular) == current:
        return acc


    if formular[current] == 'A':
        incCur()
        return parseFormular(formular, parseAnd(formular))

    elif formular[current] == 'O':
        incCur()
        return parseFormular(formular, parseOr(formular))

    elif formular[current] == 'N':
        incCur()
        return parseFormular(formular, parseNot(formular))

    elif formular[current] == 'I':
        incCur()
        return parseFormular(formular, parseImpl(formular))

    elif formular[current] == 'B':
        incCur()
        return parseFormular(formular, parseBiImpl(formular))

    elif formular[current] in string.ascii_lowercase:
        incCur()
        return parseFormular(formular, parseAtom(formular))
        
    elif formular[current] == ',':
        incCur()

        if formular[current] != " ":
            return False
        incCur()

        return acc

    elif formular[current] == ')':
        incCur()
        return acc

    else:
        return False



def firstStep(formular : Formular):
    # Cancelation Condition
    if type(formular) == str or len(formular.value) == 1:
        return formular


    
    if formular.value == "Not":

        # Involution of the Negator
        if formular.neg.value == "Not":
            
            formular = formular.neg.neg

        # DeMorgan when the inner Value is a And
        elif formular.neg.value == "And":
            
            formular = Formular("Or", Formular("Not", neg=formular.neg.left), Formular("Not", neg=formular.neg.right))

        # DeMorgan when the inner Value is a Or
        elif formular.neg.value == "Or":
            
            formular = Formular("And", Formular("Not", neg=formular.neg.left), Formular("Not", neg=formular.neg.right))            


    # Idempotenz of the Or/And Operator        
    if formular.value == "Or" or formular.value == "And":
        if str(formular.left) == str(formular.right):
            formular = formular.left


    
    
    # Make sure to loop trough the whole tree
    if formular.value == "Not":
        firstStep(formular.neg)

    formular.left = firstStep(formular.left)
    formular.right = firstStep(formular.right)

    return formular


def secondStep(formular : Formular):
    # Cancelation Condition
    if type(formular) == str or len(formular.value) == 1:
        return formular


    
    
    
    # Make sure to loop trough the whole tree
    if formular.value == "Not":
        firstStep(formular.neg)

    formular.left = firstStep(formular.left)
    formular.right = firstStep(formular.right)

    return formular

    


# tester = "Not(Not(And(Impl(Not(a), And(BiImpl(a, Not(Not(b))), b)), And(Not(b), And(Not(a), Not(a)))))))"
tester = "Not(Or(Not(a), b))"


if __name__ == '__main__':
    formular = parseFormular(tester, Formular())

    print(formular)
    print(firstStep(formular))
    print(secondStep(formular))