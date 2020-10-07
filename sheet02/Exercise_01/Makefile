EXECUTE_CMD = python3
TEST_CMD = python3 -m doctest

all: execute test

execute:
	$(EXECUTE_CMD) exercise_02_01_a.py

test:
	$(TEST_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__