#!/usr/bin/bash

# Read input scripts as array
scripts=("$@")

# Verify if there is at least one input
if [ ${#scripts[@]} -eq 0 ]; then
  echo "Usage : $0 <path/to/script_1> ... <path/to/script_n>"
  exit 1
fi

# Start the virtual environment
poetry shell

# Run the auto_dag_app
result=$(python3 ./auto_dag_app/main.py ${scripts[*]})

# Show result
echo "$result"
