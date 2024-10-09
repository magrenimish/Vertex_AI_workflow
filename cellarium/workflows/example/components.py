import kfp
from kfp import dsl
from kfp.dsl import *
from typing import *


@dsl.component(base_image="us-central1-docker.pkg.dev/broad-dsde-methods/cellarium-ai/cellarium-ml@sha256:0722fcc9364f86e826bfdc1aa1f33149e37c0c615043096a82550317c8f4aeec", 
               packages_to_install=[
                   "git+https://github.com/cellarium-ai/cellarium-ml.git@lr_with_sequential_lr_scheduler",
                   "gcsfs",
                   "tensorboard",
                   ])
def base_model_lr_run_final(config: str = "gs://cellarium-file-system/ml-configs/Supervised_cell_classification/Base_model_regular_LR/Base_model_regular_lr.yaml",
                ):
    """
    Test Example component
    """
    #import os
    from cellarium.ml.cli import main as cellarium_ml_cli
    #os.environ["NODE_RANK"] = os.environ.get("RANK")

    cellarium_ml_cli(args=["logistic_regression", "fit", "--config", config])
    
    print("LR Training is being executed....")