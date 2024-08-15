#!/usr/bin/bash

# Default user bin directory
default_bin=$HOME/.local/bin

# Default name for the auto_dag cli command
default_name="autodag"

# Symlink auto_dag.sh to ~/.local/bin if exists
# or create it if not
if [ ! -d $default_bin ]; then
  echo "Creating the $default_bin directory..."
  mkdir $default_bin

  echo "Exporting $default_bin to PATH..."
  export_str= '\n# Export ~/.local/bin to PATH\n [ "${PATH#*$default_bin:}" == "$PATH" ] && export PATH="$default_bin:$PATH"'
  case $SHELL in
    /usr/bin/bash)
      echo -e $export_str >> $HOME/.bashrc;;
    /usr/bin/zsh)
      echo -e $export_str >> $HOME/.zshrc;;
  esac

  echo "Creating the $default_name symlink..."
  ln -s $(pwd)/auto_dag.sh $default_bin/$default_name

elif [ ! -f $default_bin/$default_name ]; then
  echo "Creating the $default_name symlink..."
  ln -s $(pwd)/auto_dag.sh $default_bin/$default_name

else
  echo "The $default_bin/$default_name symlink already exists"

fi

# Restart your shell
exec $SHELL
