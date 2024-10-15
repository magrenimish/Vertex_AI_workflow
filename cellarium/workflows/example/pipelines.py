from kfp import dsl
from cellarium.workflows import kfp_helpers
from cellarium.workflows.example import components


@dsl.pipeline()
def model_3_pipeline(component_1_config: str = "gs://cellarium-file-system/ml-configs/Supervised_cell_classification/Model_3_lr_NT_Log1p_DBS/Model_3_config.yaml"):
    """
    KFP pipeline to run tdigest train pipeline.

    """
    component_job_1 = kfp_helpers.create_job(
        component_func=components.model_3,
        display_name="model_3",
        replica_count=1,
        machine_type="n1-highmem-16",
        accelerator_type = "NVIDIA_TESLA_T4",
        accelerator_count=2,
        config=component_1_config
    )


    task_1 = component_job_1()



if __name__ == '__main__':
    model_3_pipeline()
