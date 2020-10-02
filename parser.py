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
def resCur():
    global current
    current = 0


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
            >>> resCur()
            >>> res = parseFormular("And(Impl(Not(a), And(BiImpl(a, b), b)), And(Not(b), Not(a)))")
            >>> print(res)
            ((¬ ¬ a ∨ (((¬ a ∨ b) ∧ (a ∨ ¬ b)) ∧ b)) ∧ (¬ b ∧ ¬ a))
            >>> resCur()
            >>> res = parseFormular("Not(Not(And(Impl(Not(a), And(BiImpl(a, Not(Not(b))), b)), And(Not(b), And(Not(a), Not(a)))))))")
            >>> print(res)
            ¬ ¬ ((¬ ¬ a ∨ (((¬ a ∨ ¬ ¬ b) ∧ (a ∨ ¬ ¬ ¬ b)) ∧ b)) ∧ (¬ b ∧ (¬ a ∧ ¬ a)))
    """
    global current

    if len(formular) == current:
        current = 0  # Make sure to reset this variable or you can't parse other formulars
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
        current = 0  # Make sure to reset this variable or you can't parse other formulars
        return False



def convertCNF(formular : Formular) -> Formular:
    """
        This function is used to calculate the CNF of any given Formular.

        Doctests:
            >>> resCur()
            >>> res = parseFormular("And(Impl(a, b), And(Impl(c, d), Not(Impl(e, f))))")
            >>> print(convertCNF(res))
            ((¬ a ∨ b) ∧ ((¬ c ∨ d) ∧ (e ∧ ¬ f)))
            >>> resCur()
            >>> res2 = parseFormular("And(Impl(Not(a), b), And(Not(b), Not(a)))")
            >>> print(convertCNF(res2))
            ((a ∨ b) ∧ (¬ b ∧ ¬ a))
    """

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


          
    if formular.value == "Or":
        # Idempotenz of the Or Operator  
        if str(formular.left) == str(formular.right):
            formular = formular.left


        # Distributivity when (A u B) o (C u D) -> (A o (C u D)) u (B o (C u D)) -> ((A o C) u (A o D)) u ((B o C) u (B o D))
        elif formular.left.value == "And" and formular.right.value == "And":

            acc = Formular("And", 
                Formular("Or", formular.left.left, formular.right),
                Formular("Or", formular.left.right, formular.right)
                )

            formular = Formular("And", 
                Formular("And", 
                    Formular("Or", acc.left.left, acc.left.right.left),
                    Formular("Or", acc.left.left, acc.left.right.right)), 
                Formular("And",
                    Formular("Or", acc.right.left, acc.right.right.left),
                    Formular("Or", acc.right.left, acc.right.right.right))
                )



        # Distributivity when (A u B) o C -> (A o C) u (B o C)
        elif formular.left.value == "And":

            formular = Formular("And", 
                Formular("Or", formular.left.left, formular.right),
                Formular("Or", formular.left.right, formular.right)
                )

        # Distributivity when C o (A u B)  -> (C o A) u (C o B)
        elif formular.right.value == "And":

            formular = Formular("And", 
                Formular("Or", formular.left, formular.right.left),
                Formular("Or", formular.left, formular.right.right)
                )


    # Idempotenz of the And Operator  
    if formular.value == "And":
        if str(formular.left) == str(formular.right):
            formular = formular.left
    


    # Make sure to loop trough the whole tree
    if formular.value == "Not":
        convertCNF(formular.neg)

    formular.left = convertCNF(formular.left)
    formular.right = convertCNF(formular.right)

    return formular


def convertDIMACS(formular : Formular) -> Formular:
    res = []
    acc = []
    chars = []
    i = 0

    while i < len(str(formular)):

        c = str(formular)[i]        

        if c == "\u00AC":
            d = str(formular)[i] + str(formular)[i+2]
            if d not in acc: acc.append(d)  # Make sure by checking, that you don't put one Variable in which is already in 
        
            if str(formular)[i+2] not in chars: chars.append(str(formular)[i+2])  # Check if the char is already in the List, otherwise append it

            i += 2  # Make sure the Index gets increased so it won't get read again 

        elif c in string.ascii_lowercase:
            if c not in acc: acc.append(c)

            if c not in chars: chars.append(c)

        elif c == "\u2227":
            res.append(acc)
            acc = []

        i += 1

    res.append(acc)

    print("p cnf %d %d" % (len(chars), len(res)))  # Calculate the used variables and the count of the formulas

    for l in res:

        for i in l:

            if i[0] == "\u00AC":  # When there is a neg then get the index of i+1 and set a - in front
                print("-" + str(chars.index(i[1]) + 1), end=" ")
            else:
                print(chars.index(i) + 1, end=" ")  # Normal char which can be printed normally

        print("0")




def main(formular : Formular) -> str:
    """
        This function unites all the previous functions and prints out the DIMACS Format of an
        given Formular.

        Doctests:
            >>> main("And(Impl(Not(a), b), And(Not(b), Not(a)))")
            Original: ((¬ ¬ a ∨ b) ∧ (¬ b ∧ ¬ a))
            CNF:      ((a ∨ b) ∧ (¬ b ∧ ¬ a))
            <BLANKLINE>
            p cnf 2 3
            1 2 0
            -2 0
            -1 0
            >>> main("And(Impl(Not(a), And(b, c)), Or(Not(b), BiImpl(Or(Not(a), c), d)))")
            Original: ((¬ ¬ a ∨ (b ∧ c)) ∧ (¬ b ∨ ((¬ (¬ a ∨ c) ∨ d) ∧ ((¬ a ∨ c) ∨ ¬ d))))
            CNF converting failed! Retrying...
            CNF:      (((a ∨ b) ∧ (a ∨ c)) ∧ (((¬ b ∨ (a ∨ d)) ∧ (¬ b ∨ (¬ c ∨ d))) ∧ (¬ b ∨ ((¬ a ∨ c) ∨ ¬ d))))
            <BLANKLINE>
            p cnf 4 5
            1 2 0
            1 3 0
            -2 1 4 0
            -2 -3 4 0
            -2 -1 3 -4 0

    """
    resCur()  # Make sure the current counter is reseted to 0, because there can be special cases 
    acc = parseFormular(formular)
    print("Original: " + str(acc))

    cnf = convertCNF(acc)

    # Make sure there is a valid CNF, when there was a change, repeat it a often as necessary
    while str(cnf) != str(convertCNF(cnf)):
        print("CNF converting failed! Retrying...")
        cnf = convertCNF(cnf)


    print("CNF:      " + str(cnf), end="\n\n")

    convertDIMACS(cnf)


# tester = "Not(Not(And(Impl(Not(a), And(BiImpl(a, Not(Not(b))), b)), And(Not(b), And(Not(a), Not(a)))))))"
# tester = "Not(Or(Not(a), b))"
# tester = "Or(And(a, b), And(c, d))"
# test = "And(Impl(Not(a), b), And(Not(b), Not(a)))"
tester = "And(Impl(Not(a), b), And(Not(b), Not(a)))"


if __name__ == '__main__':
    # main(tester)

    # main("And(Impl(Not(a), And(b, c)), Or(Not(b), BiImpl(BiImpl(Not(a), c), d)))")
    # main("And(Impl(Not(a), b), And(Not(b), Not(a)))")
    main(tester)

    main(tester)

    main("BiImpl(Impl(Not(a), b), And(Not(b), Not(a)))")  # Noch zu testen ob das klappt
