from kfp import dsl
from cellarium.workflows import kfp_helpers
from cellarium.workflows.example import components


@dsl.pipeline()
def viscy_train_trial_1(component_1_config: str = "gs://cellarium-file-system/curriculum/viscy/configs/viscy_train_config.yaml"):
    """
    KFP pipeline to run tdigest train pipeline.

    """
    component_job_1 = kfp_helpers.create_job(
        component_func=components.viscy_train,
        display_name="viscy_traintrial_1",
        replica_count=1,
        machine_type="n1-highmem-16",
        accelerator_type = "NVIDIA_TESLA_T4",
        accelerator_count=1,
        config=component_1_config
    )


    task_1 = component_job_1()



if __name__ == '__main__':
    viscy_train_trial_1()
