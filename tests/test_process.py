import pytest
import os

from auto_dag_app.extract_and_process.process import concat_py_files
from auto_dag_app.params import TEST_PY_FILE_PROCESS_1, TEST_PY_FILE_PROCESS_2


###################################
# Set the conditions for the test #
###################################

# Path of the curent dir
dir_path = os.path.dirname(os.path.realpath(__file__))

# Full path of the first test python file for the process function
test_py_file_process_1_full = dir_path + "/" + TEST_PY_FILE_PROCESS_1

# Full path of the second test file for the process function
test_py_file_process_2_full = dir_path + "/" + TEST_PY_FILE_PROCESS_2

# Put the tests files paths inside a list
files_list = [test_py_file_process_1_full, test_py_file_process_2_full]


################################
# Testing the process function #
################################


@pytest.fixture
def mock_output() -> str:
    """Define the mock output for the test of the
    concat_py_file function."""

    return """# module name: test_file_process_1

def hello():
    print("Hello !")


# module name: test_file_process_2

from test_file_process_1 import hello

hello()


"""


def test_concat_py_files(mock_output):
    """Test if the output of the concat_py_file function
    is the same as the mock_output."""

    assert concat_py_files(files_list) == mock_output
