.PHONY: venv install test migrate revision help

VENV_DIR := venv
PYTHON    := $(VENV_DIR)/bin/python
PIP       := $(VENV_DIR)/bin/pip
ALEMBIC   := $(VENV_DIR)/bin/alembic

# Run your test suite
test: install
	$(PYTHON) -m pytest

# Generate a new migration script
# Usage: make revision MESSAGE="describe changes"
revision: install
ifndef MESSAGE
	$(error MESSAGE is undefined.  Usage: make revision MESSAGE="describe changes")
endif
	$(ALEMBIC) revision --autogenerate -m "$(MESSAGE)"

# Apply all pending migrations
migrate: install
	$(ALEMBIC) upgrade head

# Create a virtualenv
venv:
	python3 -m venv $(VENV_DIR)

# Install requirements into the venv
install: venv
	$(PIP) install -r requirements.txt

help:
	echo "make test"
	echo "make venv"
	echo "make install"
	echo "make revision MESSAGE=\"describe migration here\""

