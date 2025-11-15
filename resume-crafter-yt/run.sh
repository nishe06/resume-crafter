#!/bin/bash

# Navigate to the project directory
cd "$(dirname "$0")"

# Activate virtual environment
source ../venv/bin/activate

# Run the Flask application
python app.py

