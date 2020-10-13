
EXECUTE_CMD = python3
TEST_CMD = python3 -m doctest

all: execute test

execute:
	$(EXECUTE_CMD) create_pddl.py > problem.pddl
	./../downward-main/fast-downward.py domain.pddl problem.pddl --search "astar(blind())"

test:
	$(TEST_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__