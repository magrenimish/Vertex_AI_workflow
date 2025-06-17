# Vertex AI Workflows Example for Viscy training
This codes contains helper functions and example to train the VSUNet (UNeXt2_2D) model in Vertex AI platform (powered by Kubeflow) with config file, and training data accessed from GCS buckets as well as training checkpoints saved to a GCS bucket.

The current workflow makes use of an n1-highmem-16 machine with 1 NVIDIA_TESLA_T4 GPU.

Following is a description of the base image I used and the package versions:
- Base Image: us-central1-docker.pkg.dev/dsp-cell-annotation-service/cellarium-ml/gpt2:pykeops
    - Python: 3.11.4
    - CUDA: 11.8
    - PyTorch: 2.0.1
    - torchvision: 0.15.2
    - OS: Ubuntu 22.04
    - Pip: 23.2.1
    - GPU Support: Yes (CUDA, torch.cuda.is_available() == True)

The Viscy repository cloned that includes code to read and write to GCS buckets is available at https://github.com/magrenimish/VisCy
