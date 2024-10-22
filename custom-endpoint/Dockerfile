# Use NVIDIA's PyTorch container as a base image
FROM --platform=$BUILDPLATFORM nvcr.io/nvidia/pytorch:24.08-py3

# Set the working directory
WORKDIR /workspace

# Install additional Python packages
RUN pip install transformers peft fastapi uvicorn

# Copy the FastAPI server script into the container
COPY ./fastapi_server.py /workspace/fastapi_server.py

# Expose the port for FastAPI
EXPOSE 8000

# Create the entrypoint script for serving the model
COPY ./entrypoint.sh /workspace/entrypoint.sh
RUN chmod +x /workspace/entrypoint.sh

# Set the entrypoint to start FastAPI
ENTRYPOINT ["/workspace/entrypoint.sh"]
