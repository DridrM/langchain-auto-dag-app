import sys

from auto_dag_app.create_dag.create_dag import create_mermaid_dag_from_scripts
from auto_dag_app.params import GPT_MODEL_PARAMS_DICT
from auto_dag_app.preprompt import DAG_GENERATION_PREPROMPT

# Execute the create_mermaid_dag_from_script function
if __name__ == "__main__":
    # Read the arguments (python file paths)
    file_list = sys.argv[1:]

    # Call the function
    graph = create_mermaid_dag_from_scripts(
        file_list,
        machine_template=DAG_GENERATION_PREPROMPT,
        model_params=GPT_MODEL_PARAMS_DICT,
    )

    # Print the result
    print(graph)
