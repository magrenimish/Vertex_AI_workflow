from kfp import dsl
from cellarium.workflows import kfp_helpers
from cellarium.workflows.example import components


@dsl.pipeline()
def base_model_no_pp_hop_score_calculation_trial_2_final(component_1_config: str = "gs://cellarium-file-system/ml-configs/lrexp_human_validation/Base_model_regular_lr_no_pp/Base_model_no_pp_prediction_config.yaml"):
    """
    KFP pipeline to run tdigest train pipeline.

    """
    component_job_1 = kfp_helpers.create_job(
        component_func=components.base_model_no_pp_hop_score_calculation_trial_2,
        display_name="base_model_no_pp_hop_score_calculation_trial_2_final",
        replica_count=5,
        machine_type="n1-highmem-32",
        #accelerator_type = "NVIDIA_TESLA_T4",
        accelerator_count=1,
        config=component_1_config
    )


    task_1 = component_job_1()



if __name__ == '__main__':
    base_model_no_pp_hop_score_calculation_trial_2_final()
