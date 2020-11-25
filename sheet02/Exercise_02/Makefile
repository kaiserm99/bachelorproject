# Copyright 2020, University of Freiburg
# Bachelor-project - Foundations of Artificial Intelligence

# Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>


EXECUTE_CMD = python3
TEST_CMD = python3 -m doctest

all: execute test

execute:
	$(info **********************  Exercise 1 **********************)
	$(info Printing the shortest path from Frankfurt to München in the given transition system...)
	$(EXECUTE_CMD) shortest_path.py

test:
	$(TEST_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__