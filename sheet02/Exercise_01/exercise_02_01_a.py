#!/usr/bin/env python3

"""
Copyright 2020, University of Freiburg
Bachelor-project - Foundations of Artificial Intelligence

Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>

Description:

Usage:

"""

from constraint import *


def main():
    problem = Problem()

    domain = [0, 1, 2]
    variables = ["WA", "NT", "Q", "NSW", "V", "SA", "T"]

    problem.addVariables(variables, domain)

    # All constraints
    problem.addConstraint(lambda x, y: x != y, ("WA", "NT"))
    problem.addConstraint(lambda x, y: x != y, ("WA", "SA"))
    problem.addConstraint(lambda x, y: x != y, ("NT", "SA"))
    problem.addConstraint(lambda x, y: x != y, ("NT", "Q"))
    problem.addConstraint(lambda x, y: x != y, ("SA", "Q"))
    problem.addConstraint(lambda x, y: x != y, ("SA", "NSW"))
    problem.addConstraint(lambda x, y: x != y, ("SA", "V"))
    problem.addConstraint(lambda x, y: x != y, ("Q", "NSW"))
    problem.addConstraint(lambda x, y: x != y, ("V", "NSW"))


    for n, sol in enumerate(problem.getSolutions()):
        print(("%d. Solution:") % (n+1))
        print(sol, end="\n\n")


if __name__ == '__main__':
    main()




