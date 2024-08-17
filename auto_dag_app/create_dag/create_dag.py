from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate

from auto_dag_app.extract_and_process.process import concat_py_files


def create_mermaid_dag_from_scripts(
    files_list: list, machine_template: str, model_params: dict
):
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
    # Note: the openai_api_key arg is no longer needed with this version of
    # langchain, because it directly reed the api key from environment variables
    chat_model = ChatOpenAI(**model_params)

    # Create the chat prompt
    chat_prompt = ChatPromptTemplate.from_messages(
        [("system", machine_template), ("human", human_template)]
    )

    # Construct the prompt message
    messages = chat_prompt.format_messages(text=py_files_str)

    # Invoke the llm response
    response = chat_model.invoke(messages)

    return response.content
