#!/bin/bash

# Use the `uname` command to get the name of the operating system
OS=$(uname)

# Check the value of the `OS` variable to determine the operating system
if [ "$OS" = "Linux" ]; then
	# Execute Linux-specific commands
	echo "Running on Linux"
	curl -o requirements.txt https://github.com/eco-gy/eco-gy-client/blob/main/requirements.txt
	curl -o main.py https://github.com/eco-gy/eco-gy-client/blob/main/main.py
	python -m venv venv
	source bin/venv/activate
	pip install -r requirements.txt
	python main.py
elif [ "$OS" = "Darwin" ]; then
  # Execute Mac-specific commands
  echo "Running on Mac"
elif [ "$OSTYPE" = "msys" ]; then
  # Execute Windows-specific commands
  echo "Running on Windows"
  # Download the requirements.txt file from GitHub
	curl -o requirements.txt https://github.com/eco-gy/eco-gy-client/blob/main/requirements.txt

	# Download the main.py file from GitHub
	curl -o main.py https://github.com/eco-gy/eco-gy-client/blob/main/main.py

	# Create a new virtual environment using the `venv` module
	python -m venv venv

	# Activate the virtual environment
	venv\Scripts\activate

	# Install the required packages from the requirements.txt file
	pip install -r requirements.txt

	# Execute the main.py script
	python main.py
else
  # Handle other operating systems
  echo "Running on unknown operating system"
fi


#mkdir ecogy-client
#cd ecogy-client

