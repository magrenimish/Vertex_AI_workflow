import kfp
from kfp import dsl
from kfp.dsl import *
from typing import *

@dsl.component(
    base_image="us-central1-docker.pkg.dev/dsp-cell-annotation-service/cellarium-ml/gpt2:pykeops",
    packages_to_install=[
        "gcsfs",
        "ome-zarr",
        "git+https://github.com/magrenimish/VisCy.git"
    ]
)
def viscy_train(config: str = "gs://cellarium-file-system/curriculum/viscy/configs/viscy_train_config.yaml"):
    import subprocess
    import os
    import gcsfs

    # Use safe writeable auth path
    auth_dir = "/tmp/auth"
    os.makedirs(auth_dir, exist_ok=True)
    key_path = os.path.join(auth_dir, "key.json")

    # Download GCP key from GCS using gcsfs
    fs = gcsfs.GCSFileSystem()
    with fs.open("gs://cellarium-file-system/curriculum/viscy/configs/spheric-keel-462917-m6-a9db4afb1241.json", "rb") as src, open(key_path, "wb") as dst:
        dst.write(src.read())

    # Set GOOGLE_APPLICATION_CREDENTIALS for access
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

    # Optional: Confirm environment setup
    subprocess.run("python --version", shell=True, check=True)
    subprocess.run("pip list", shell=True, check=True)

    # Run the VisCy CLI command
    subprocess.run(f"viscy fit --config gs://viscy/viscy_train_config.yaml", shell=True, check=True)

    print("Training completed")
