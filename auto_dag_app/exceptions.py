class ExtensionError(Exception):
    """This exception is raised inside the extract function
    from the extract_and_process package, and indicate the file
    you want to extract the text from doesn't have a python
    extension."""
