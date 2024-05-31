import sys

file_name = sys.argv[1]

def extract(file_name: str) -> str:
    """Extract the content of a python file (.py) and
    transform it into a string.
    Arguments:
    - file_name: the name of the python file (.py)"""

    file_str = ""

    with open(file_name, mode = "r") as file:
        for line in file:
            file_str += line + "\n"

    return file_str
