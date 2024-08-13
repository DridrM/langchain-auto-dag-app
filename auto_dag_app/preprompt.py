# Prepromt instructions for generating the DAG
DAG_GENERATION_PREPROMPT = (
    "Write a script in Mermaid corresponding to a directed acyclic graph. "
    "This directed acyclic graph should represent the relationships between "
    "all the objects created in the following Python script. The created "
    "objects are thoose preceded by the keyword 'class' for the custom objects "
    "and by 'def' for the custom functions. Note that the following input script "
    "is an aggregation of several Python scripts situated in different modules. "
    "The modules are indicated behind a '#' sign above the the functions or "
    "objects that belong to that module. For each module, show the relationships "
    "between objects, functions, and highlight the module logic. Don't link the "
    "parameters imported from the 'params' module to the other functions or "
    "objects."
)
