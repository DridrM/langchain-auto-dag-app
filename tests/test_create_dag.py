import pytest
import os

from auto_dag_app.create_dag.create_dag import create_mermaid_dag_from_scripts
from auto_dag_app.params import (
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

    test_files_path = "/home/bender/Code/DridrM/personal_data_projects/renewable_energy_forecast/re_forecast/data"
    test_file_process_path_1 = test_files_path + "/" + "load_data.py"
    test_file_process_path_2 = test_files_path + "/" + "format_data.py"
    test_file_process_path_3 = test_files_path + "/" + "store_data.py"
    test_file_process_path_4 = test_files_path + "/" + "manage_data_storage.py"
    test_file_process_path_5 = test_files_path + "/" + "read_data.py"
    test_file_process_path_6 = test_files_path + "/" + "utils.py"
    test_file_process_path_7 = test_files_path + "/" + "get_data.py"
    files_list = [
        test_file_process_path_1,
        test_file_process_path_2,
        test_file_process_path_3,
        test_file_process_path_4,
        test_file_process_path_5,
        test_file_process_path_6,
        test_file_process_path_7,
    ]

    return files_list


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
