import pytest
import os

from auto_dag_app.extract_and_process.extract import extract
from auto_dag_app.exceptions import ExtensionError
from auto_dag_app.params import TEST_PY_FILE_EXTRACT, TEST_FAKE_FILE_EXTRACT


###################################
# Set the conditions for the test #
###################################

# Path of the curent dir
dir_path = os.path.dirname(os.path.realpath(__file__))

# Full path of the test python file for the extract function
test_py_file_extract_full = dir_path + "/" + TEST_PY_FILE_EXTRACT

# Full path of the fake test file for the extract function
test_fake_file_extract_full = dir_path + "/" + TEST_FAKE_FILE_EXTRACT


################################################
# Testing function(s) for the extract function #
################################################

def test_extract_py_file():
    """Test if the extract function output a string given
    as a python file path."""

    assert isinstance(extract(test_py_file_extract_full), str)

def test_extract_other_file():
    """Test if the extract function raise an error when
    the file is not a python file."""

    with pytest.raises(ExtensionError):
        extract(test_fake_file_extract_full)
