from kfp import dsl


@dsl.component(base_image="python:3.10-slim")
def logistic_regression_component(config: str):
    """
    Test Example component
    """
    import os 
    import subprocess
    command = f"cellarium-ml custom_logistic_regression fit --config '{config}'"
    subprocess.run(command, shell=True, check=True)
    print("Example logistic regression component is being executed....")