from kfp import dsl
from cellarium.workflows import kfp_helpers
from cellarium.workflows.example import components


@dsl.pipeline()
def base_model_670_targets_no_pp_65_trial_1(component_1_config: str = "gs://cellarium-file-system/ml-configs/lrexp_human_validation/Base_model_670_targets_no_pp/Base_model_670_targets_no_pp_65.yaml"):
    """
    KFP pipeline to run tdigest train pipeline.

    """
    component_job_1 = kfp_helpers.create_job(
        component_func=components.base_model_670_targets_no_pp_65,
        display_name="base_model_670_targets_no_pp_65_trial_1",
        replica_count=1,
        machine_type="n1-highmem-16",
        accelerator_type = "NVIDIA_TESLA_T4",
        accelerator_count=1,
        config=component_1_config
    )


    task_1 = component_job_1()



if __name__ == '__main__':
    base_model_670_targets_no_pp_65_trial_1()
