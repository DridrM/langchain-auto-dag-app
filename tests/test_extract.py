import os

from auto_dag_app.extract_and_process.extract import extract
from auto_dag_app.params import TEST_FILE_EXTRACT


###################################
# Set the conditions for the test #
###################################

# Path of the curent dir
dir_path = os.path.dirname(os.path.realpath(__file__))

#


def test_extract():
    """"""
    # assert
