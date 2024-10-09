from kfp import dsl
from cellarium.workflows import kfp_helpers
from cellarium.workflows.example import components


@dsl.pipeline()
def base_model_lr_pipeline_final(component_1_config: str = "gs://cellarium-file-system/ml-configs/Supervised_cell_classification/Base_model_regular_LR/Base_model_regular_lr.yaml"):
    """
    KFP pipeline to run tdigest train pipeline.

    """
    component_job_1 = kfp_helpers.create_job(
        component_func=components.base_model_lr_run_final,
        display_name="base_model_lr_run_final",
        replica_count=1,
        machine_type="n1-highmem-16",
        accelerator_type = "NVIDIA_TESLA_T4",
        accelerator_count=2,
        config=component_1_config
    )


    task_1 = component_job_1()



if __name__ == '__main__':
    base_model_lr_pipeline()
