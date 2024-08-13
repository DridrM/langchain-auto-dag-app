import os


###########################################################################
# Params from the environment variables: Interaction with the Open AI API #
###########################################################################

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


####################################
# Params for the create_dag module #
####################################

# Parameters for the GPT model
GPT_MODEL_PARAMS_DICT = {"model": "gpt-4o", "temperature": 0.7, "cache": False}


#####################
# Unit tests params #
#####################

# Path of the python test file for the extract step
TEST_PY_FILE_EXTRACT = "test_files/test_file_extract.py"

# Path of the fake python test file for the extract step
TEST_FAKE_FILE_EXTRACT = "test_files/fake_test_file_extract.txt"

# Path of the first python test file for the process step
TEST_PY_FILE_PROCESS_1 = "test_files/test_file_process_1.py"

# Path of the second python test file for the process step
TEST_PY_FILE_PROCESS_2 = "test_files/test_file_process_2.py"
