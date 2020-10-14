
EXECUTE_CMD = python3
TEST_CMD = python3 -m doctest

all: execute test

execute:
	$(EXECUTE_CMD) create_pddl.py kami.txt > problem.pddl
	./../downward-main/fast-downward.py domain.pddl problem.pddl --search "astar(blind())"

	# ./../downward-main/fast-downward.py domain.pddl problem.pddl --evaluator "hff=ff()" --evaluator "hcea=cea()" --search "lazy_greedy([hff, hcea], preferred=[hff, hcea])"
	
	# ./../downward-main/fast-downward.py domain.pddl problem.pddl --evaluator "hcea=cea()" --search "lazy_greedy([hcea], preferred=[hcea])"

test:
	$(TEST_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__