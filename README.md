# Langchain auto DAG app project

## Overview
Document a project can be tedious, espacialy the larger the project is.
In the same time, understanding the structure of the larger project can be a very useful knowledge ressource to start a new project.
Indeed, you can use an existing structure as a canvas, use specific parts of an existinng structure or improve an existing structure for a new project.
In order to achieve this work automatically, I had the idea to use LLM to track function dependencies between each other within a project scripts.
After tracking all the dependencies, the LLM will then produce a directed acyclic graph of the dependencies  in the form of a script in the Mermaid language.

## Structure of the project
<ins>The project is divided in two parts :</ins>

- [extract_an_process](https://github.com/DridrM/langchain-auto-dag-app/tree/master/auto_dag_app/extract_and_process) : Extract python files from list of paths, process them as strings and stack them together.
- [create_dag](https://github.com/DridrM/langchain-auto-dag-app/tree/master/auto_dag_app/create_dag) : Read the python scripts as a stack string and with the help of the Langchain library and the OpenAI API, generate a script in the Mermaid language corresponding to an acyclilc graph of the interactions of the functions and objects within their modules, corresponding to the inner structure of the project where belong the python scripts.

<ins>There is also these importants files used to customize the behavior of the app :</ins>

- [params.py](https://github.com/DridrM/langchain-auto-dag-app/blob/master/auto_dag_app/params.py) : You can find here the dict with the OpenAI model parameters such as the GPT model version (currently GPT 4o) and the temperature argument conditioning the variability in the model output (currently 0.7). You can change all these arguments and add others.
- [prepromt.py](https://github.com/DridrM/langchain-auto-dag-app/blob/master/auto_dag_app/preprompt.py) : The preprompt containing the instructions to the GPT model to follow in order to understand the scripts and generate the desired output.

## Tools used
The main tool used in this project is Langchain for Python. This is a library aimed to interact with LLM APIs or local LLMs and used to build application around
the possibilities given by LLMs.

## How to install and run the project
<ins>Follow these steps :</ins>

0) Clone the curent repository using `gh repo clone https://github.com/DridrM/langchain-auto-dag-app/tree/master`
1) [Create an OpenAI account and create an OPENAI_API_KEY](https://platform.openai.com/docs/quickstart)
2) Create a .env file inside the project directory and paste it the `OPENAI_API_KEY` (with this exact name)
3) [Install pyenv and poetry](https://douwevandermeij.medium.com/proper-python-setup-with-pyenv-poetry-4d8baea329a8)
4) [Install direnv and hook it into your .bashrc or .zshrc](https://direnv.net/)
5) [Install python 3.12 with pyenv](https://douwevandermeij.medium.com/proper-python-setup-with-pyenv-poetry-4d8baea329a8)
6) [Make python 3.12 local to your project directory](https://douwevandermeij.medium.com/proper-python-setup-with-pyenv-poetry-4d8baea329a8)
7) [Indicate poetry to use python 3.12 with this command in your terminal (linux systems):](https://douwevandermeij.medium.com/proper-python-setup-with-pyenv-poetry-4d8baea329a8) `poetry env use $(pyenv which python)`
8) Create the virtual environment with `poetry shell`
9) Inside the shell, install all the requirements and the project configuration with `poetry install`
10) Leave the shell with `exit`, and run these commands : `chmod +x install.sh` and `chmod +x auto_dag.sh`. The `install.sh` file is used to create the command line interface. The `auto_dag.sh` is the interface between the command line tool and the main python script.
11) Execute the `install.sh` file with `bash install.sh` or `./install.sh`.

You are now ready to use the command line tool.

## How to use the project
Simply type inside your shell `autodag path/to/script_1 path/to/script_2 ... path/to/script_n` with the paths to the python scripts of your project.


![Tests](https://github.com/DridrM/langchain-auto-dag-app/actions/workflows/run_tests.yaml/badge.svg)
