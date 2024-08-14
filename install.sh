#!/usr/bin/bash

# Default user bin directory
default_bin=$HOME/.local/bin

# Symlink auto_dag.sh to ~/.local/bin if exists
# or create it if not
if [ ! -d $default_bin ]; then
  mkdir $default_bin
elif [ ! -f $default_bin/auto_dag.sh ]; then
  ln -s $(pwd)/auto_dag.sh $default_bin/auto_dag.sh
else
  echo "The $default_bin/auto_dag.sh symlink already exists"
fi

# Alias auto_dag.sh in your aliases file
# if exists else in your zshrc or your bashrc
dotfiles=$(find $HOME -name dotfiles -type d)
aliases=$(find $dotfiles -name aliases -type f)
alias_str="\n# auto_dag cli tool : Create a graphical map of your software project\nalias adag=$default_bin/auto_dag.sh"

if [[ -d $dotfiles && -f $aliases ]]; then
  echo -e $alias_str >> $aliases
else
  case $SHELL in
    /usr/bin/bash)
      echo -e $alias_str >> $HOME/.bashrc;;
    /usr/bin/zsh)
      echo -e $alias_str >> $HOME/.zshrc;;
  esac
fi

# Restart your shell
exec $SHELL
