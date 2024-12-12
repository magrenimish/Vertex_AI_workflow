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
def model_variation_4_hop_score_calculation(config: str = "gs://cellarium-file-system/ml-configs/lrexp_human_validation/Model_variation_4/model_4_prediction_config.yaml",
                ):
    """
    Test Example component
    """
    #import os
    from cellarium.ml.cli import main as cellarium_ml_cli
    #os.environ["NODE_RANK"] = os.environ.get("RANK")

    cellarium_ml_cli(args=["custom_logistic_regression", "predict", "--config", config])
    
    print("LR Training is being executed....")