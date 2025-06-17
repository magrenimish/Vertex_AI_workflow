FROM us-central1-docker.pkg.dev/dsp-cell-annotation-service/cellarium-ml/gpt2:pykeops
USER root
ENV DEBIAN_FRONTEND=noninteractive

# Install system packages
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    build-essential \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Verify Python and pip versions (optional but good practice)
RUN python --version && python3 --version && pip --version

# Upgrade build tools
RUN pip install --upgrade pip setuptools wheel

# Install your packages
RUN pip install \
    "git+https://github.com/magrenimish/VisCy.git" \
    "viscy" \
    "viscy[metrics]" \
    "viscy[visual]" \
    "gcsfs" \
    "ome-zarr" \
    "six" \
    "pyparsing"

# Install CUDA libraries
RUN pip install \
    nvidia-cublas-cu12==12.6.4.1 \
    nvidia-cuda-cupti-cu12==12.6.80 \
    nvidia-cuda-nvrtc-cu12==12.6.77 \
    nvidia-cuda-runtime-cu12==12.6.77 \
    nvidia-cudnn-cu12==9.5.1.17 \
    nvidia-cufft-cu12==11.3.0.4 \
    nvidia-cufile-cu12==1.11.1.6 \
    nvidia-curand-cu12==10.3.7.77 \
    nvidia-cusolver-cu12==11.7.1.2 \
    nvidia-cusparse-cu12==12.5.4.2 \
    nvidia-cusparselt-cu12==0.6.3 \
    nvidia-nccl-cu12==2.26.2 \
    nvidia-nvjitlink-cu12==12.6.85 \
    nvidia-nvtx-cu12==12.6.77

# Set default working directory
WORKDIR /workspace

# Set CUDA environment variables
ENV NVIDIA_VISIBLE_DEVICES=all \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility \
    CUDA_DEVICE_ORDER=PCI_BUS_ID

CMD ["/bin/bash"]
