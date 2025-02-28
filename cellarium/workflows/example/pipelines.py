from kfp import dsl
from cellarium.workflows import kfp_helpers
from cellarium.workflows.example import components


@dsl.pipeline()
def Model_variation_5_alpha_zero_normalized_hop_score_calculation_trial_1(component_1_config: str = "gs://cellarium-file-system/ml-configs/lrexp_human_validation/Model_5_alpha_zero_normalized/model_5_alpha_zero_normalization_prediction_config.yaml"):
    """
    KFP pipeline to run tdigest train pipeline.

    """
    component_job_1 = kfp_helpers.create_job(
        component_func=components.model_variation_5_alpha_zero_normalized_hop_score_calculation_trial_1,
        display_name="model_variation_5_alpha_zero_normalized_hop_score_calculation_trial_1",
        replica_count=1,
        machine_type="n1-highmem-16",
        accelerator_type = "NVIDIA_TESLA_T4",
        accelerator_count=1,
        config=component_1_config
    )


    task_1 = component_job_1()



if __name__ == '__main__':
    Model_variation_5_alpha_zero_normalized_hop_score_calculation_trial_1()
