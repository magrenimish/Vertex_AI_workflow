import click

from cellarium.workflows.example import pipelines
from cellarium.workflows import kfp_helpers


@click.command()
@click.option("--project_id")
@click.option("--location")
@click.option("--display_name")
@click.option("--component_1_config")
def submit_example(project_id: str = "dsp-cell-annotation-service", location: str = "us-central1", display_name: str = "model_variation_5_alpha_zero_no_normalization_hop_score_calculation", component_1_config: str = "gs://cellarium-file-system/ml-configs/lrexp_human_validation/Model_5_alpha_zero_no_normalization/model_5_alpha_zero_no_normalization_prediction_config.yaml"):
    kfp_helpers.submit_pipeline(
        pipeline_func=pipelines.Model_variation_5_alpha_zero_no_normalization_hop_score_calculation,
        project_id=project_id,
        location=location,
        pipeline_display_name=display_name,
        pipeline_kwargs={"component_1_config": component_1_config}
    )
    print("Submitted pipeline!")


if __name__ == "__main__":
    submit_example()
