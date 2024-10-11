import kfp
from kfp import dsl
from kfp.dsl import *
from typing import *


@dsl.component(base_image="us-central1-docker.pkg.dev/dsp-cell-annotation-service/cas-services-cicd/cas-pytorch-cuda-pipeline-dev:1.4.5-alpha.1", 
               packages_to_install=[
                   "anndata==0.10.9",
                   "git+https://github.com/cellarium-ai/cellarium-ml.git@lr_sequential_lr_ontology_cells",
                   "gcsfs",
                   ])
def base_model_lr_run_final(config: str = "gs://cellarium-file-system/ml-configs/Supervised_cell_classification/Base_model_regular_LR/Base_model_regular_lr_final.yaml",
                ):
    """
    Test Example component
    """
    #import os
    from cellarium.ml.cli import main as cellarium_ml_cli
    #os.environ["NODE_RANK"] = os.environ.get("RANK")

    cellarium_ml_cli(args=["logistic_regression", "fit", "--config", config])
    
    print("LR Training is being executed....")