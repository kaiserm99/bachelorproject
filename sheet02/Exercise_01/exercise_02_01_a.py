from constraint import *

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

problem.addConstraint(lambda x, y: x != y, ("NSW", "V"))
problem.addConstraint(lambda x, y: x != y, ("NSW", "SA"))
problem.addConstraint(lambda x, y: x != y, ("NSW", "Q"))

problem.addConstraint(lambda x, y: x != y, ("SA", "WA"))
problem.addConstraint(lambda x, y: x != y, ("SA", "NT"))





print(len(problem.getSolutions()))





