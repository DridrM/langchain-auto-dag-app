#!/usr/bin/bash

# Read input scripts
read -p "Enter python scripts paths : " -a scripts

# Start the virtual environment
poetry shell

# Run the auto_dag_app
result=$(python3 ./auto_dag_app/main.py ${scripts[*]})

# Show result
echo "$result"
