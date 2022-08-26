PYTHON_VENV ?= $(PWD)/.venv
BUILD_ROOT ?= $(PWD)/build

run-python-venv=(. $(PYTHON_VENV)/bin/activate && $1)

pyenv:
	python3 -m venv $(PYTHON_VENV)
	chmod +x $(PYTHON_VENV)/bin/activate

.PHONY: install-deps
install-deps:
	$(call run-python-venv, pip3 install -r requirements.txt)

.PHONY: update-deps
update-deps:
	$(call run-python-venv, pip-compile requirements.in > requirements.txt)

.PHONY: setup
setup: pyenv install-deps
	$(call run-python-venv, pre-commit install)

.PHONY: check
check:
	$(call run-python-venv, python -m isort --check --diff $(ISORT_ARGS) **/*.py)
	$(call run-python-venv, black --check **/*.py)
	$(call run-python-venv, flake8 **/*.py)

.PHONY: format
format:
	$(call run-python-venv, python -m isort **/*.py)
	$(call run-python-venv, black **/*.py)

.PHONY: test
test:
	$(call run-python-venv, python -m unittest discover -f --start-directory=tests --pattern "*.py")

.PHONY: coverage
coverage:
	$(call run-python-venv, coverage erase)
	$(call run-python-venv, coverage run -m unittest discover -f --start-directory=tests --pattern "*.py")
	$(call run-python-venv, coverage report -m)

.PHONY: build
build:
	mkdir -p $(BUILD_ROOT)
	python3 setup.py install --root=$(BUILD_ROOT) --prefix=/usr

.PHONY: publish
publish:
	$(call run-python-venv, python setup.py upload)
