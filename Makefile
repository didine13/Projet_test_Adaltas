# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 utils/*.py

black:
	@black utils/*.py tests/*.py

test:
	@coverage run -m pytest tests/test_utils.py

clean:
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__ .pytest_cache
	@rm -fr *.egg-info build

install:
	@pip install . -U

all: clean install black check_code test
