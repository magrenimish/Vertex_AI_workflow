import subprocess
import kfp
from kfp import dsl
from kfp.dsl import *
from typing import *



@dsl.component(base_image="docker.io/nimishmagre1996/viscy-py311-cuda12:latest")
def viscy_train(config: str = "gs://cellarium-file-system/curriculum/viscy/configs/viscy_train_config.yaml",
                ):
    """
    Test Example component
    """
    """
    Vertex AI component to run viscy CLI via subprocess call.
    """
    # Construct the CLI command
    import subprocess
    cmd = ["viscy", "fit", "--c", config]

    # Run the command
    subprocess.run(cmd, check=True)
    
    print("LR Training is being executed....")