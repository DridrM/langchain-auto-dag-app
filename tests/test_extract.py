import pytest
import os

from auto_dag_app.extract_and_process.extract import extract
from auto_dag_app.params import TEST_FILE_EXTRACT


###################################
# Set the conditions for the test #
###################################

# Path of the curent dir
dir_path = os.path.dirname(os.path.realpath(__file__))

# Full path of the test file for the extract function
test_file_extract_full = dir_path + "/" + TEST_FILE_EXTRACT


################################################
# Testing function(s) for the extract function #
################################################

def test_extract():
    """Test if the extract function output a string given
    as a python file path."""

    assert isinstance(extract(test_file_extract_full), str)
