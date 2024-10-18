import kfp
from kfp import dsl
from kfp.dsl import *
from typing import *


@dsl.component(base_image="us-central1-docker.pkg.dev/dsp-cell-annotation-service/cas-services-cicd/cas-pytorch-cuda-pipeline-dev:1.4.5-alpha.1", 
               packages_to_install=[
                   "anndata==0.10.9",
                   "git+https://github.com/cellarium-ai/cellarium-ml.git@logistic_regression_variation_5",
                   "gcsfs",
                   ])
def model_5(config: str = "gs://cellarium-file-system/ml-configs/Supervised_cell_classification/Model_5_lr_NT_Log1p_DBS/Model_5_alpha_0.5_config.yaml",
                ):
    """
    Test Example component
    """
    #import os
    from cellarium.ml.cli import main as cellarium_ml_cli
    #os.environ["NODE_RANK"] = os.environ.get("RANK")

    cellarium_ml_cli(args=["custom_logistic_regression", "fit", "--config", config])
    
    print("LR Training is being executed....")