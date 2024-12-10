import click

from cellarium.workflows.example import pipelines
from cellarium.workflows import kfp_helpers


@click.command()
@click.option("--project_id")
@click.option("--location")
@click.option("--display_name")
@click.option("--component_1_config")
def submit_example(project_id: str = "dsp-cell-annotation-service", location: str = "us-central1", display_name: str = "base_model_no_pp_hop_score_calculation_final", component_1_config: str = "gs://cellarium-file-system/ml-configs/lrexp_human_validation/Base_model_regular_lr_no_pp/Base_model_no_pp_prediction_config.yaml"):
    kfp_helpers.submit_pipeline(
        pipeline_func=pipelines.base_model_no_pp_hop_score_calculation_final,
        project_id=project_id,
        location=location,
        pipeline_display_name=display_name,
        pipeline_kwargs={"component_1_config": component_1_config}
    )
    print("Submitted pipeline!")


if __name__ == "__main__":
    submit_example()
