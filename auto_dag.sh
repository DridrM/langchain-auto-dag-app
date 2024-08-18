#!/usr/bin/zsh

# Default name for the auto_dag cli command
# If you change the default name here, pleas make sure
# to do the same inside the install.sh file
default_name="autodag"

# Read input scripts as array
scripts=("$@")

# Verify if there is at least one input
if [ ${#scripts[@]} -eq 0 ]; then
  echo "Usage : $default_name <path/to/script_1> ... <path/to/script_n>"
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
