EXECUTE_CMD = python3
TEST_CMD = python3 -m doctest

all: execute test

execute:
	$(EXECUTE_CMD) shortest_path.py

test:
	$(TEST_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__