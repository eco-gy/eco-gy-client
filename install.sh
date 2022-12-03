#!/bin/bash

# Use the `uname` command to get the name of the operating system
OS=$(uname)

# Check the value of the `OS` variable to determine the operating system
if [ "$OS" = "Linux" ]; then
	# Execute Linux-specific commands
	echo "Running on Linux"
	curl -o requirements.txt https://raw.githubusercontent.com/eco-gy/eco-gy-client/main/requirements.txt
	curl -o run.sh https://raw.githubusercontent.com/eco-gy/eco-gy-client/main/run.sh
	curl -o main.py https://raw.githubusercontent.com/eco-gy/eco-gy-client/main/main.py
	python3 -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	./run.sh
elif [ "$OS" = "Darwin" ]; then
  # Execute Mac-specific commands
  echo "Running on Mac"
elif [ "$OSTYPE" = "msys" ]; then
  # Execute Windows-specific commands
  echo "Running on Windows"
  # Download the requirements.txt file from GitHub
	curl -o requirements.txt https://raw.githubusercontent.com/eco-gy/eco-gy-client/main/requirements.txt
	curl -o run.sh https://raw.githubusercontent.com/eco-gy/eco-gy-client/main/run.sh
	curl -o main.py https://raw.githubusercontent.com/eco-gy/eco-gy-client/main/main.py
	# Create a new virtual environment using the `venv` module
	python -m venv venv
	# Activate the virtual environment
	venv\Scripts\activate
	# Install the required packages from the requirements.txt file
	pip install -r requirements.txt
	# Execute the main.py script
	.\run.sh
else
  # Handle other operating systems
  echo "Running on unknown operating system"
fi
