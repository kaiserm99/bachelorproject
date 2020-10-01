EXECUTE_CMD = python3.7
TEST_CMD = python3 -m doctest
CHECKSTYLE_CMD = flake8

all: execute test checkstyle

execute:
	$(EXECUTE_CMD) parser.py

test:
	$(TEST_CMD) *.py

checkstyle:
	$(CHECKSTYLE_CMD) *.py

clean:
	rm -f *.pyc
	rm -rf __pycache__
