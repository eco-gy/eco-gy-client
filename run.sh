#!/bin/bash

# Use the `uname` command to get the name of the operating system
OS=$(uname)

# Check the value of the `OS` variable to determine the operating system
if [ "$OS" = "Linux" ]; then
	# Execute Linux-specific commands
	echo "Running on Linux"
	python3 -m venv venv
	source venv/bin/activate
	python main.py
elif [ "$OS" = "Darwin" ]; then
	# Execute Mac-specific commands
	echo "Running on Mac"
  	python3 -m venv venv
	source venv/bin/activate
	python main.py
elif [ "$OSTYPE" = "msys" ]; then
	# Execute Windows-specific commands
	echo "Running on Windows"
	# Create a new virtual environment using the `venv` module
	python -m venv venv
	# Activate the virtual environment
	venv\Scripts\activate
	# Install the required packages from the requirements.txt file
	pip install -r requirements.txt
else
  # Handle other operating systems
  echo "Running on unknown operating system"
fi
