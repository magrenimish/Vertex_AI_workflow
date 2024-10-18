from kfp import dsl
from cellarium.workflows import kfp_helpers
from cellarium.workflows.example import components


@dsl.pipeline()
def model_5_pipeline(component_1_config: str = "gs://cellarium-file-system/ml-configs/Supervised_cell_classification/Model_5_lr_NT_Log1p_DBS/Model_5_alpha_0.5_config.yaml"):
    """
    KFP pipeline to run tdigest train pipeline.

    """
    component_job_1 = kfp_helpers.create_job(
        component_func=components.model_5,
        display_name="model_5_alpha_0.5",
        replica_count=1,
        machine_type="n1-highmem-16",
        accelerator_type = "NVIDIA_TESLA_T4",
        accelerator_count=2,
        config=component_1_config
    )


    task_1 = component_job_1()



if __name__ == '__main__':
    model_5_pipeline()
