default: tests

tests:
	pytest

test_ep_cov:
	pytest --cov=./auto_dag_app/extract_and_process
