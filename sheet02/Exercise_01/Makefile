# Copyright 2020, University of Freiburg
# Bachelor-project - Foundations of Artificial Intelligence

# Author: Marco Kaiser <kaiserm@informatik.uni-freiburg.de>


EXECUTE_CMD = python3
TEST_CMD = python3 -m doctest

all: execute_1 execute_2 test

execute_1:
	$(info **********************  Exercise 1 **********************)
	$(info Printing all the possible coloring of Australia when using three colors...)
	$(EXECUTE_CMD) exercise_02_01_a.py

execute_2:
	$(info **********************  Exercise 2 **********************)
	$(info Starting a game of Minesweeper with the Dimension of 15 and 15 Bombs...)
	$(EXECUTE_CMD) minesweeper_main.py --fast --board 15 15

test:
	$(TEST_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__