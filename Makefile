# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 project/*.py

black:
	@black project/*.py

test:
	@coverage run -m pytest tests/*.py

clean:
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__ .pytest_cache
	@rm -fr *.egg-info

install:
	@pip install . -U

all: clean install black check_code test
