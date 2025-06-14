FROM nvidia/cuda:12.6.2-devel-ubuntu22.04
ENV DEBIAN_FRONTEND=noninteractive
# Install Python 3.11 and pip
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get update && apt-get install -y \
    python3.11 \
    python3.11-dev \
    python3.11-distutils \
    curl \
    && curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

# Set python3 and pip to point to python3.11 and pip3.11
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1 \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1 \
    && update-alternatives --install /usr/bin/pip pip /usr/local/bin/pip3.11 1

# Check versions (optional)
RUN python --version && pip --version

# Set Python version and install base system packages
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    wget \
    git \
    curl \
    build-essential \
    ca-certificates \
    python3.11 \
    python3.11-venv \
    python3.11-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install pip/setuptools build tools
RUN pip install --upgrade pip setuptools wheel

RUN pip install --upgrade pip

# Now install your package
RUN pip install "git+https://github.com/magrenimish/VisCy.git"
# Install viscy and extras
RUN pip install \
    "viscy" \
    "viscy[metrics]" \
    "viscy[visual]" \
    gcsfs \
    ome-zarr


# Install CUDA dependencies
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

# Default working directory
WORKDIR /workspace
# Force system-wide defaults to Python 3.11
RUN ln -sf /usr/bin/python3.11 /usr/bin/python && \
    ln -sf /usr/bin/python3.11 /usr/local/bin/python && \
    ln -sf /usr/local/bin/pip3.11 /usr/bin/pip && \
    ln -sf /usr/local/bin/pip3.11 /usr/local/bin/pip
RUN apt-get purge -y python3.10 python3.10-minimal||true

# Set environment variables to enable CUDA
ENV NVIDIA_VISIBLE_DEVICES=all \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility \
    CUDA_DEVICE_ORDER=PCI_BUS_ID

CMD ["/bin/bash"]
