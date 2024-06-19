from auto_dag_app.extract_and_process.extract import extract_py_files


def concat_py_files(files_list: list) -> str:
    """Extract python files from .py files given a list of files paths.
    Transform each python file into a string.
    Concatenate python files as strings in one big string.
    Inside the big string, python files are separated from each
    other by their file name in commentary
    Argument:
    - files_list: the list of .py files paths"""

    concat_file = ""

    for file_name in files_list:
        module_path, file_str = extract_py_files(file_name)
        module_name = module_path.split("/")[-1].strip(".py")
        concat_file += f"# module name: {module_name}\n\n" + f"{file_str}\n\n"

    return concat_file
