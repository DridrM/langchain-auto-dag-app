import sys

from auto_dag_app.exceptions import ExtensionError


def extract(file_name: str) -> str:
    """Extract the content of a python file (.py) and
    transform it into a string.
    Arguments:
    - file_name: the name of the python file (.py)"""

    # Assure that the file has the .py extension
    if not file_name.endswith(".py"):
        raise ExtensionError("The file doesn't have a python extension.")

    file_str = ""

    with open(file_name, mode = "r") as file:
        for line in file:
            file_str += line + "\n"

    return file_str
