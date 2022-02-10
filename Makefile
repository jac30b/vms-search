PYTHON=python3
TEST_DIR = tests/

run:
	${PYTHON} main.py

test:
	cd ${TEST_DIR} && ${PYTHON} -m pytest
