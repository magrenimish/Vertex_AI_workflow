from kfp import dsl
from cellarium.workflows import kfp_helpers
from cellarium.workflows.example import components


@dsl.pipeline()
def Model_variation_5_alpha_zero_no_normalization_hop_score_calculation(component_1_config: str = "gs://cellarium-file-system/ml-configs/lrexp_human_validation/Model_5_alpha_zero_no_normalization/model_5_alpha_zero_no_normalization_prediction_config.yaml"):
    """
    KFP pipeline to run tdigest train pipeline.

    """
    component_job_1 = kfp_helpers.create_job(
        component_func=components.model_variation_5_alpha_zero_no_normalization_hop_score_calculation,
        display_name="model_variation_5_alpha_zero_no_normalization_hop_score_calculation",
        replica_count=1,
        machine_type="n1-highmem-32",
        accelerator_type = "NVIDIA_TESLA_T4",
        accelerator_count=2,
        config=component_1_config
    )


    task_1 = component_job_1()



if __name__ == '__main__':
    Model_variation_5_alpha_zero_no_normalization_hop_score_calculation()
