#!/usr/bin/zsh

# Read input scripts as array
scripts=("$@")

# Verify if there is at least one input
if [ ${#scripts[@]} -eq 0 ]; then
  echo "Usage : $0 <path/to/script_1> ... <path/to/script_n>"
  exit 1
fi

# Execute script in the auto_dag project directory
cd $AUTODAGPATH

# This command allow direnv to work in the sub-process
eval "$(direnv export zsh)"

# Run the auto_dag_app
results=$(poetry run python3 auto_dag_app/main.py ${scripts[*]})

# Show result
echo "$results"
