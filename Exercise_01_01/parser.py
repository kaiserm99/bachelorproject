#!/usr/bin/env python3

"""
Copyright 2020, University of Freiburg
Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

Usage of the Script:


"""
# parser.py, written on: Donnerstag,  1 Oktober 2020.


import string

class Formular:
    def __init__(self, value = "init", left = "-", right = "-", neg = "-", atom = False, top = False, bot = False):
        self.value = value
        self.left = left
        self.right = right
        self.neg = neg
        self.atom = atom
        self.top = top
        self.bot = bot

    def __str__(self):
        
        if self.value == "Not":
            acc = "\u00AC " + str(self.neg)
            
        elif self.atom:
            acc = self.value
            
        elif self.value == "And":
            acc = "(" + str(self.left) + " \u2227 " + str(self.right) + ")"

        elif self.value == "Or":
            acc = "(" + str(self.left) + " \u2228 " + str(self.right) + ")"

        elif self.top:
            acc = "\u22A4"

        elif self.bot:
            acc = "\u22A5"

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
            print("False!")
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
                    Formular("Or", Formular("Not", neg=left), right), 
                    Formular("Or", left, Formular("Not", neg=right)))



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
    # Check if the Atom has any more lowercase letters and parse them
    acc = formular[current - 1]
    running = True

    while running:
        c = formular[current]

        if c == ")" or c == ",":
            running = False
        else:
            acc += c
            incCur()  # Only increment when there is a ) or a , because the next char which is going to get parsed should be one of those chars

        

    return Formular(acc, atom=True)


def parseTop(formular : Formular) -> Formular:
    # Check if the Word is spelled correctly
    for c in "OP":
        if formular[current] != c:
            return False
        incCur()

    return Formular("TOP", top=True)


def parseBot(formular : Formular) -> Formular:
    # Check if the Word is spelled correctly
    for c in "OT":
        if formular[current] != c:
            return False
        incCur()

    return Formular("BOT", bot=True)



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

    # If the given acc -> the formular which get parsed next, is not valid, return False to all
    if not acc:
        return False

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

        if formular[current] == 'O':
            return parseFormular(formular, parseBot(formular))
        else:
            return parseFormular(formular, parseBiImpl(formular))

    elif formular[current] in string.ascii_lowercase:
        incCur()
        return parseFormular(formular, parseAtom(formular))

    elif formular[current] == 'T':
        incCur()
        return parseFormular(formular, parseTop(formular))

    elif formular[current] == 'B':
        incCur()
        return parseFormular(formular, parseBot(formular))
        
    elif formular[current] == ',':
        incCur()

        if formular[current] != " ":  # Skip the blank line
            return False
        incCur()

        return acc

    elif formular[current] == ')':
        incCur()
        return acc

    else:  # This should never get triggered, just in case
        current = 0  # Make sure to reset this variable or you can't parse other formulars
        return False



def convertCNF(formular : Formular) -> Formular:
    """
        This function is used to calculate the CNF of any given Formular.

        Note:
            This function isn't perfect, because of the BiImpl. The correctness is haneled
            in convertDIMACS!

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
    if type(formular) == str or formular.atom:
        return formular

    
    if formular.value == "Not":
        # Neg(⊤) -> ⊥
        if formular.neg.top:
            formular = Formular("BOT", bot=True)

        # Neg(⊥) -> ⊤
        elif formular.neg.bot:
            formular = Formular("TOP", top=True)

        # Involution of the Negator
        elif formular.neg.value == "Not":
            
            formular = formular.neg.neg

        # DeMorgan when the inner Value is a And
        elif formular.neg.value == "And":
            
            formular = Formular("Or", Formular("Not", neg=formular.neg.left), Formular("Not", neg=formular.neg.right))

        # DeMorgan when the inner Value is a Or
        elif formular.neg.value == "Or":
            
            formular = Formular("And", Formular("Not", neg=formular.neg.left), Formular("Not", neg=formular.neg.right))            


          
    if formular.value == "Or":
        # Or(⊤, Formular) or Or(Formular, ⊤) or Or(⊤, ⊤) --> ⊤
        if formular.left.top or formular.right.top:
            formular = Formular("TOP", top=True)

        # Or(⊥, ⊥) --> ⊥
        elif formular.left.bot and formular.right.bot:
            formular = Formular("BOT", bot=True)

        # Or(⊥, Formular) --> Formular
        elif formular.left.bot:
            formular = formular.right

        # Or(Formular, ⊥) --> Formular
        elif formular.right.bot:
            formular = formular.left

        # Idempotenz of the Or Operator  
        elif str(formular.left) == str(formular.right):
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

  
    if formular.value == "And":
        # And(⊥, Formular) or And(Formular, ⊥) or And(⊥, ⊥) --> ⊥
        if formular.left.bot and formular.right.bot:
            formular = Formular("BOT", bot=True)

        # Or(⊤, ⊤) --> ⊤
        elif formular.left.bot and formular.right.bot:
            formular = Formular("TOP", top=True)

        # Or(⊤, Formular) --> Formular
        elif formular.left.top:
            formular = formular.right

        # Or(Formular, ⊤) --> Formular
        elif formular.right.top:
            formular = formular.left

        # Idempotenz of the And Operator
        elif str(formular.left) == str(formular.right):
            formular = formular.left
    


    # Make sure to loop trough the whole tree
    if formular.value == "Not":
        convertCNF(formular.neg)

    formular.left = convertCNF(formular.left)
    formular.right = convertCNF(formular.right)

    return formular


def getAtom(formular : str, i : int) -> tuple:
    acc = formular[i]
    running = True

    while running:

        c = formular[i+1]  # Index shift becaue the i-te char has already been read

        if c not in string.ascii_lowercase:
            running = False
        else:
            acc += c
            i += 1

    return (acc, i)


def convertDIMACS(formular : Formular) -> Formular:
    if formular.top:
        print("This is a valid Formular! No need to print the DIMACS-Format!")
        return

    elif formular.bot:
        print("This is a unvalid Formular! No need to print the DIMACS-Format!")
        return


    res = []
    acc = []
    variables = []
    str_form = str(formular)
    i = 0

    while i < len(str(formular)):

        c = str_form[i]

        if c == "\u00AC":  # If there is a neg char
            # Format: i = neg, i+1 = BLANK, i+2 = Atom beginning

            d = str_form[i]

            atom, i = getAtom(str_form, i+2)  # Because of the format an index shift

            d += atom

            if d not in acc: acc.append(d)  # Make sure by checking, that you don't put one Variable in which is already in 
        
            if atom not in variables: variables.append(atom)  # Check if the atom is already in the List, otherwise append it


        elif c in string.ascii_lowercase:  # If you read a lowercase char, then it is a Atom and check how long it continues
            
            atom, i = getAtom(str_form, i)

            if atom not in acc: acc.append(atom)

            if atom not in variables: variables.append(atom)

        elif c == "\u2227":  # If there is a and Symbol, append the current set
            res.append(acc)
            acc = []

        i += 1

    res.append(acc)  # Make sure the last set is also appended because there is no and symbol

    variables.sort()  # Make sure the char set is sorted so it is easier to comprehend the Result

    print("p cnf %d %d" % (len(variables), len(res)))  # Calculate the used variables and the count of the formulas

    # Loop trogh everey set of sets and check which char is shown at the moment
    for l in res:

        for i in l:

            if i[0] == "\u00AC":  # When there is a neg then get the index of i+1 and set a - in front
                print("-" + str(variables.index(i[1:]) + 1), end=" ")
            else:
                print(variables.index(i) + 1, end=" ")  # Normal char which can be printed normally

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

    if type(acc) is bool:
        print("The Syntax of the given Formula is false!")
        return

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
# tester = "And(Impl(Not(a), b), And(Not(b), Not(a)))"


if __name__ == '__main__':
    # main(tester)

    main("And(Impl(Not(a), And(b, quer)), Or(Not(BOT), BiImpl(BiImpl(Not(a), TOP), b)))")
    # main("And(Impl(Not(a), b), And(Not(b), Not(a)))")
    # main(tester)

    # main(tester)

    # main("BiImpl(Impl(Not(a), b), And(Not(b), Not(a)))")

    main("And(Or(And(asdfest, TOP), Or(TOP, Or(a, b))), BOT)")
