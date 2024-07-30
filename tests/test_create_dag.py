import pytest
import os

from auto_dag_app.create_dag.create_dag import create_mermaid_dag_from_scripts
from auto_dag_app.params import (
    TEST_PY_FILE_PROCESS_1,
    TEST_PY_FILE_PROCESS_2,
    DAG_GENERATION_PREPROMPT,
    OPENAI_API_KEY,
    GPT_MODEL_PARAMS_DICT,
)


################################
# Testing the process function #
################################


@pytest.fixture
def mock_input() -> list:
    """Create a list of files to test the
    create_mermaid_dag_from_scripts"""

    # Path of the curent dir
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Full path of the first test python file for the process function
    test_py_file_process_1_full = dir_path + "/" + TEST_PY_FILE_PROCESS_1

    # Full path of the second test file for the process function
    test_py_file_process_2_full = dir_path + "/" + TEST_PY_FILE_PROCESS_2

    # Put the tests files paths inside a list
    files_list = [test_py_file_process_1_full, test_py_file_process_2_full]

    return files_list


# Skip the test because it requires the open_ai_api_key. The test only run in local
# but failed when executed by github actions.
@pytest.skip(
    reason="Fail when executed by github actions, because requires the open_ai_api_key"
)
def test_create_mermaid_dag_from_scripts(mock_input):
    """Test if the create_mermaid_dag_from_scripts
    function output a string"""

    response = create_mermaid_dag_from_scripts(
        mock_input,
        machine_template=DAG_GENERATION_PREPROMPT,
        openai_api_key=OPENAI_API_KEY,
        model_params=GPT_MODEL_PARAMS_DICT,
    )
    assert isinstance(response, str)
