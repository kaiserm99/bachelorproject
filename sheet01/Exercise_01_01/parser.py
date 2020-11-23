#!/usr/bin/env python3

"""
Copyright 2020, University of Freiburg
Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

Usage of the Script:


"""
# parser.py, written on: Donnerstag,  1 Oktober 2020.

import sys, string

# Only use if needed more recursion depth
# =======================================
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
# sys.setrecursionlimit(10**6)

class Formula:
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


DEBUG = False
current = 0


def incCur():
    global current
    current += 1


def resCur():
    global current
    current = 0


def parseOr(formula : Formula) -> Formula:
    # Check if the Word is spelled correctly
    for c in "r(":
        if formula[current] != c:
            return False
        incCur()
        
    left = parseFormula(formula)
    right = parseFormula(formula)

    if left is False or right is False:
        return False

    return Formula("Or", left, right)


def parseAnd(formula : Formula) -> Formula:
    # Check if the Word is spelled correctly
    for c in "nd(":
        if formula[current] != c:
            print("False!")
            return False
        incCur()
        
    left = parseFormula(formula)  
    right = parseFormula(formula)

    if left is False or right is False:
        return False

    return Formula("And", left, right)


# A -> B --> -A o B
def parseImpl(formula : Formula) -> Formula:
    # Check if the Word is spelled correctly
    for c in "mpl(":
        if formula[current] != c:
            return False
        incCur()
        
    left = parseFormula(formula)
    right = parseFormula(formula)

    if left is False or right is False:
        return False

    return Formula("Or", Formula("Not", neg=left), right)



# A <-> B --> (-A o B) u () (A o -B)
def parseBiImpl(formula : Formula) -> Formula:
    # Check if the Word is spelled correctly
    for c in "iImpl(":
        if formula[current] != c:
            return False
        incCur()
        
    left = parseFormula(formula)
    right = parseFormula(formula)

    if left is False or right is False:
        return False

    return Formula("And",
                    Formula("Or", Formula("Not", neg=left), right), 
                    Formula("Or", left, Formula("Not", neg=right)))



def parseNot(formula : Formula) -> Formula:
    # Check if the Word is spelled correctly
    for c in "ot(":
        if formula[current] != c:
            return False
        incCur()
        
    value = parseFormula(formula)

    if value is False:
        return False

    return Formula("Not", neg = value)



def parseAtom(formula) -> Formula:
    # Check if the Atom has any more lowercase letters and parse them
    acc = formula[current - 1]
    running = True

    while running:
        c = formula[current]

        if c == ")" or c == ",":
            running = False
        else:
            acc += c
            incCur()  # Only increment when there is a ) or a , because the next char which is going to get parsed should be one of those chars

    return Formula(acc, atom=True)


def parseTop(formula : Formula) -> Formula:
    # Check if the Word is spelled correctly
    for c in "OP":
        if formula[current] != c:
            return False
        incCur()

    return Formula("TOP", top=True)


def parseBot(formula : Formula) -> Formula:
    # Check if the Word is spelled correctly
    for c in "OT":
        if formula[current] != c:
            return False
        incCur()

    return Formula("BOT", bot=True)



def parseFormula(formula : str, acc = Formula) -> Formula:
    """ 
        This function is used to parse the whole formula which is given by an string.
        The global Variable current takes care of which letter is used at the moment.
        This function takes care of the Implications and the Äquvalations and replaces
        it directly.

        Doctests:
            >>> resCur()
            >>> res = parseFormula("And(Impl(Not(a), And(BiImpl(a, b), b)), And(Not(b), Not(a)))")
            >>> print(res)
            ((¬ ¬ a ∨ (((¬ a ∨ b) ∧ (a ∨ ¬ b)) ∧ b)) ∧ (¬ b ∧ ¬ a))
            >>> resCur()
            >>> res = parseFormula("Not(Not(And(Impl(Not(a), And(BiImpl(a, Not(Not(b))), b)), And(Not(b), And(Not(a), Not(a)))))))")
            >>> print(res)
            ¬ ¬ ((¬ ¬ a ∨ (((¬ a ∨ ¬ ¬ b) ∧ (a ∨ ¬ ¬ ¬ b)) ∧ b)) ∧ (¬ b ∧ (¬ a ∧ ¬ a)))
    """
    global current

    # If the given acc -> the formula which get parsed next, is not valid, return False to all
    if not acc:
        return False

    if len(formula) == current:
        current = 0  # Make sure to reset this variable or you can't parse other formulas
        return acc


    if formula[current] == 'A':  # And()
        incCur()
        return parseFormula(formula, parseAnd(formula))

    elif formula[current] == 'O':  # Or()
        incCur()
        return parseFormula(formula, parseOr(formula))

    elif formula[current] == 'N':  # Not()
        incCur()
        return parseFormula(formula, parseNot(formula))

    elif formula[current] == 'I':  # Impl()
        incCur()
        return parseFormula(formula, parseImpl(formula))

    elif formula[current] == 'B':
        incCur()

        if formula[current] == 'O':  # BOT
            return parseFormula(formula, parseBot(formula))
        else:  # BiImpl()
            return parseFormula(formula, parseBiImpl(formula))

    elif formula[current] in string.ascii_lowercase:  # atom
        incCur()
        return parseFormula(formula, parseAtom(formula))

    elif formula[current] == 'T':  # TOP
        incCur()
        return parseFormula(formula, parseTop(formula))
        
    elif formula[current] == ',':
        incCur()

        if formula[current] != " ":  # Skip the blank line
            return False
        incCur()

        return acc  # Return if one of the two break conditions takes place -> in this the left side of a formula got fully parsed and now the creted Syntax tree gets returned

    elif formula[current] == ')':
        incCur()
        return acc  # Return the right side of the recursive Formula

    
    else:  # This should never get triggered, just in case
        current = 0  # Make sure to reset this variable or you can't parse other formulas
        return False



def convertCNF(formula : Formula) -> Formula:
    """
        This function is used to calculate the CNF of any given Formula.

        Note:
            This function isn't perfect, because of the BiImpl. The correctness is handled
            in convertDIMACS!

        Doctests:
            >>> resCur()
            >>> res = parseFormula("And(Impl(a, b), And(Impl(c, d), Not(Impl(e, f))))")
            >>> print(convertCNF(res))
            ((¬ a ∨ b) ∧ ((¬ c ∨ d) ∧ (e ∧ ¬ f)))
            >>> resCur()
            >>> res = parseFormula("And(Impl(Not(a), b), And(Not(b), Not(a)))")
            >>> print(convertCNF(res))
            ((a ∨ b) ∧ (¬ b ∧ ¬ a))
    """

    # Break Condition
    if type(formula) == str or formula.atom:
        return formula

    
    if formula.value == "Not":
        # Neg(⊤) -> ⊥
        if formula.neg.top:
            formula = Formula("BOT", bot=True)

        # Neg(⊥) -> ⊤
        elif formula.neg.bot:
            formula = Formula("TOP", top=True)

        # Involution of the Negator
        elif formula.neg.value == "Not":
            
            formula = formula.neg.neg

        # DeMorgan when the inner Value is a And
        elif formula.neg.value == "And":
            
            formula = Formula("Or", Formula("Not", neg=formula.neg.left), Formula("Not", neg=formula.neg.right))

        # DeMorgan when the inner Value is a Or
        elif formula.neg.value == "Or":
            
            formula = Formula("And", Formula("Not", neg=formula.neg.left), Formula("Not", neg=formula.neg.right))            


          
    if formula.value == "Or":
        # Or(⊤, Formula) or Or(Formula, ⊤) or Or(⊤, ⊤) --> ⊤
        if formula.left.top or formula.right.top:
            formula = Formula("TOP", top=True)

        # Or(⊥, ⊥) --> ⊥
        elif formula.left.bot and formula.right.bot:
            formula = Formula("BOT", bot=True)

        # Or(⊥, Formula) --> Formula
        elif formula.left.bot:
            formula = formula.right

        # Or(Formula, ⊥) --> Formula
        elif formula.right.bot:
            formula = formula.left

        # Idempotenz of the Or Operator  
        elif str(formula.left) == str(formula.right):
            formula = formula.left


        # Distributivity when (A u B) o (C u D) -> (A o (C u D)) u (B o (C u D)) -> ((A o C) u (A o D)) u ((B o C) u (B o D))
        elif formula.left.value == "And" and formula.right.value == "And":

            acc = Formula("And", 
                Formula("Or", formula.left.left, formula.right),
                Formula("Or", formula.left.right, formula.right)
                )

            formula = Formula("And", 
                Formula("And", 
                    Formula("Or", acc.left.left, acc.left.right.left),
                    Formula("Or", acc.left.left, acc.left.right.right)), 
                Formula("And",
                    Formula("Or", acc.right.left, acc.right.right.left),
                    Formula("Or", acc.right.left, acc.right.right.right))
                )



        # Distributivity when (A u B) o C -> (A o C) u (B o C)
        elif formula.left.value == "And":

            formula = Formula("And", 
                Formula("Or", formula.left.left, formula.right),
                Formula("Or", formula.left.right, formula.right)
                )

        # Distributivity when C o (A u B)  -> (C o A) u (C o B)
        elif formula.right.value == "And":

            formula = Formula("And", 
                Formula("Or", formula.left, formula.right.left),
                Formula("Or", formula.left, formula.right.right)
                )

  
    if formula.value == "And":
        # And(⊥, Formula) or And(Formula, ⊥) or And(⊥, ⊥) --> ⊥
        if formula.left.bot and formula.right.bot:
            formula = Formula("BOT", bot=True)

        # Or(⊤, ⊤) --> ⊤
        elif formula.left.bot and formula.right.bot:
            formula = Formula("TOP", top=True)

        # Or(⊤, Formula) --> Formula
        elif formula.left.top:
            formula = formula.right

        # Or(Formula, ⊤) --> Formula
        elif formula.right.top:
            formula = formula.left

        # Idempotenz of the And Operator
        elif str(formula.left) == str(formula.right):
            formula = formula.left
    


    # Make sure to loop trough the whole tree
    if formula.value == "Not":
        convertCNF(formula.neg)

    formula.left = convertCNF(formula.left)
    formula.right = convertCNF(formula.right)

    return formula


def getAtom(formula : str, i : int) -> tuple:
    """
        This function gets the full atom if convertDIMAS has found a atom and needs to 
        know the full name of it. Make sure to only use lowercase ascii atoms, otherwise
        this will fail.
    """
    acc = formula[i]
    running = True

    while running:

        c = formula[i+1]  # Index shift becaue the i-te char has already been read

        if c not in string.ascii_lowercase:
            running = False
        else:
            acc += c
            i += 1

    return (acc, i)


def convertDIMACS(formula : Formula):
    """
        This function gets a Formula which is in CNF and converts it into the DIMACS-Format
        so we can print it and we can pass it into Minisat to get the Modells of the given
        Formula.

        Doctests:
            >>> formula_str = "And(Impl(Not(a), And(b, c)), Or(Not(b), BiImpl(Or(Not(a), c), d)))"
            >>> formula = parseFormula(formula_str)
            >>> cnf = convertCNF(formula)
            >>> convertDIMACS(cnf)
            ['a', 'b', 'c', 'd']
            p cnf 4 5
            1 2 0
            1 3 0
            -2 1 0
            -3 4 0
            -2 -1 3 -4 0

            Here you can see a Example that the Function convertCNF is not perfect and you need
            to pass the created cnf through the convertCNF another time.
            >>> formula_str = "BiImpl(a, BiImpl(a, b))"
            >>> formula = parseFormula(formula_str)
            >>> cnf = convertCNF(formula)
            >>> convertDIMACS(cnf)
            ['a', 'b']
            p cnf 2 5
            -1 2 0
            -1 1 -2 0
            1 0
            -2 -1 0
            2 0
        
        Returns:
            This function do not return anything. It just prints the full DIMACS-Format of the
            given CNF and the arrangement of all the given atoms, so you can take a look which
            of the numbers corresponds to the given atom.
    """

    # Check the given Formula and based on what it is, print an Error or the DIMACS-Format
    # This is to prevent Errors which can occure because the parsing of the atom can
    # be out of Index and a Exception can get triggered.

    if formula.top:
        print("This is a tautology! No need to print the DIMACS-Format!")
        return

    elif formula.bot:
        print("This is a unsatisfiable Formula! No need to print the DIMACS-Format!")
        return

    elif formula.atom:  # If the Formula is only one atom, then print the following
        print("p cnf 1 1\n1 0")
        return

    try:
        if formula.neg.atom:  # If the Formula is onle one negetaed atom
            print("p cnf 1 1\n-1 0")
            return
    except:
        pass

    # Checking of the Formula end. Now move on to parse it and get the DIMACS-Format
    # ===============================================================================

    res = []
    acc = []
    variables = []
    str_form = str(formula)
    i = 0

    while i < len(str(formula)):

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
    print(variables)

    print("p cnf %d %d" % (len(variables), len(res)))  # Calculate the used variables and the count of the formulas

    # Loop trogh everey set of sets and check which char is shown at the moment
    for l in res:

        for i in l:

            if i[0] == "\u00AC":  # When there is a neg then get the index of i+1 and set a - in front
                print("-" + str(variables.index(i[1:]) + 1), end=" ")
            else:
                print(variables.index(i) + 1, end=" ")  # Normal char which can be printed normally

        print("0")




def main(formula : Formula) -> str:
    """
        This function unites all the previous functions and prints out the DIMACS Format of an
        given Formula.

        Doctests:
            >>> main("And(Impl(Not(a), b), And(Not(b), Not(a)))")
            ['a', 'b']
            p cnf 2 3
            1 2 0
            -2 0
            -1 0

            >>> main("And(Impl(Not(a), And(b, c)), Or(Not(b), BiImpl(Or(Not(a), c), d)))")
            ['a', 'b', 'c', 'd']
            p cnf 4 5
            1 2 0
            1 3 0
            -2 1 4 0
            -2 -3 4 0
            -2 -1 3 -4 0

            >>> main("Or(asdf, Or(asdf, Or(asdf, asdf)))")
            p cnf 1 1
            1 0

    """
    resCur()  # Make sure the current counter is reseted to 0, because there can be special cases 
    acc = parseFormula(formula)

    if DEBUG: print("Original: " + str(acc))

    if type(acc) is bool:
        print("The Syntax of the given Formula is false!")
        return

    cnf = convertCNF(acc)

    # Make sure there is a valid CNF, when there was a change, repeat it a often as necessary
    while str(cnf) != str(convertCNF(cnf)):
        cnf = convertCNF(cnf)



    if DEBUG: print("CNF:      " + str(cnf), end="\n\n")

    convertDIMACS(cnf)


# tester = "Not(Not(And(Impl(Not(a), And(BiImpl(a, Not(Not(b))), b)), And(Not(b), And(Not(a), Not(a)))))))"
# tester = "Not(Or(Not(a), b))"
# tester = "Or(And(a, b), And(c, d))"
# tester = "And(Impl(Not(a), b), And(Not(b), Not(a)))"
tester = "And(Impl(Not(a), b), Or(BiImpl(b, Or(a, And(c, d))), Not(a)))"


if __name__ == '__main__':
    # main(tester)

    # main("And(Impl(Not(a), And(b, quer)), Or(Not(BOT), BiImpl(BiImpl(Not(a), TOP), b)))")
    # main("And(Impl(Not(a), b), And(Not(b), Not(a)))")
    # main(tester)
    

    # This is the whole term for solving the given NSP in Exercise 01 d)
    # main("And(Or(fritzfo, fritzso), And(Or(fritzft, fritzst), And(Or(fridafo, fridaso), And(Or(fridaft, fridast), And(Or(udofo, Or(udoso, udono)), And(Or(udoft, Or(udost, udont)), And(Or(irafo, iraso), And(Or(iraft, irast), And(Or(heinzfo, Or(heinzso, heinzno)), And(Or(heinzft, Or(heinzst, heinznt)), And(norano, And(norant, And(BiImpl(fritzfo, fridafo), And(BiImpl(fritzso, fridaso), And(BiImpl(fritzft, fridaft), And(BiImpl(fritzst, fridast), And(BiImpl(fritzfo, Not(fritzso)), And(BiImpl(fritzso, Not(fritzfo)), And(BiImpl(fritzft, Not(fritzst)), And(BiImpl(fritzst, Not(fritzft)), And(BiImpl(fridafo, Not(fridaso)), And(BiImpl(fridaso, Not(fridafo)), And(BiImpl(fridaft, Not(fridast)), And(BiImpl(fridast, Not(fridaft)), And(BiImpl(heinzfo, Not(Or(heinzso, heinzno))), And(BiImpl(heinzso, Not(Or(heinzfo, heinzno))), And(BiImpl(heinzno, Not(Or(heinzfo, heinzso))), And(BiImpl(heinzft, Not(Or(heinzst, heinznt))), And(BiImpl(heinzst, Not(Or(heinzft, heinznt))), And(BiImpl(heinznt, Not(Or(heinzft, heinzst))), And(BiImpl(udofo, Not(Or(udoso, udono))), And(BiImpl(udoso, Not(Or(udofo, udono))), And(BiImpl(udono, Not(Or(udofo, udoso))), And(BiImpl(udoft, Not(Or(udost, udont))), And(BiImpl(udost, Not(Or(udoft, udont))), And(BiImpl(udont, Not(Or(udoft, udost))), And(BiImpl(irafo, Not(iraso)), And(BiImpl(iraso, Not(irafo)), And(BiImpl(iraft, Not(irast)), And(BiImpl(irast, Not(iraft)), And(BiImpl(heinzno, Not(udono)), And(BiImpl(udono, Not(heinzno)), And(BiImpl(heinznt, Not(udont)), And(BiImpl(udont, Not(heinznt)), And(Impl(fridafo, Not(Or(heinzfo, Or(udofo, irafo)))), And(Impl(fridaso, Not(Or(heinzso, Or(udoso, iraso)))), And(Impl(fridaft, Not(Or(heinzft, Or(udoft, iraft)))), And(Impl(fridast, Not(Or(heinzst, Or(udost, irast)))), And(Impl(heinzno, Not(heinzft)), Impl(udono, Not(udoft)))))))))))))))))))))))))))))))))))))))))))))))))))")

    main("BiImpl(a, BiImpl(a, b))")
    

