import sys
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate

from auto_dag_app.extract_and_process.process import concat_py_files
from auto_dag_app.params import (
    OPENAI_API_KEY,
    DAG_GENERATION_PREPROMPT,
    GPT_MODEL_PARAMS_DICT,
)


def create_mermaid_dag_from_scripts(
    files_list: list, machine_template: str, openai_api_key: str, model_params: dict
) -> str:
    """Generate a directed acyclic graph (DAG) representing the structure of a
    python project splited in several scripts interacting with each other.
    The DAG output is a script in the Mermaid langage. The DAG is generated
    using the ChatGPT API through the langchain library.
    Arguments:
    - files_list: a list of files paths representing the python project
    - machine_template: the pre-prompt for the ChatGPT instance
    - openai_api_key: the key to access the Open AI API service
    - model_params: dictionnary containing the GPT model parameters"""

    # Transform the py files into str from the py files paths
    py_files_str = concat_py_files(files_list)

    # Create a human template
    human_template = "{text}"

    # Instanciate a chat model
    chat_model = ChatOpenAI(openai_api_key=openai_api_key, **model_params)

    # Create the chat prompt
    chat_prompt = ChatPromptTemplate.from_messages(
        [("system", machine_template), ("human", human_template)]
    )

    # Construct the prompt message
    messages = chat_prompt.format_messages(text=py_files_str)

    # Invoke the llm response
    response = chat_model.invoke(messages)

    return response.content


# Execute the create_mermaid_dag_from_script function
if __name__ == "__main__":
    # Read the arguments (python file paths)
    file_list = sys.argv[1:]

    # Call the function
    create_mermaid_dag_from_scripts(
        file_list,
        machine_template=DAG_GENERATION_PREPROMPT,
        openai_api_key=OPENAI_API_KEY,
        model_params=GPT_MODEL_PARAMS_DICT,
    )
