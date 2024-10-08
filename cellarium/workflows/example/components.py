import kfp
from kfp import dsl
from kfp.dsl import *
from typing import *


@dsl.component(base_image="gcr.io/deeplearning-platform-release/pytorch-gpu.py310", 
               packages_to_install=[
                   "git+https://github.com/cellarium-ai/cellarium-ml",
                   "gcsfs",
                   "tensorboard",
                   ])
def base_model_lr_run(config: str = "gs://cellarium-file-system/ml-configs/Supervised_cell_classification/Base_model_regular_LR/Base_model_regular_lr.yaml",
                ):
    """
    Test Example component
    """
    import os
    from cellarium.ml.cli import main as cellarium_ml_cli
    #os.environ["NODE_RANK"] = os.environ.get("RANK")

    cellarium_ml_cli(args=["logistic_regression", "fit", "--config", config])
    
    print("LR Training is being executed....")