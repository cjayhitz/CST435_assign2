# Use an official Python base image with MPI support
FROM python:3.9-slim

# Install required dependencies including development tools for MPI
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libopenmpi-dev \
    openmpi-bin \
    && rm -rf /var/lib/apt/lists/*

# Install mpi4py and numpy
RUN pip install mpi4py numpy

# Set the working directory
WORKDIR /usr/src/app

# Copy the MPI program and the dataset into the container
COPY mpi_program.py .
COPY large_dataset.txt .

# Create a non-root user and switch to that user
RUN useradd -m mpiuser
USER mpiuser

# Update the CMD to run the mpi program as a non-root user
CMD ["mpirun", "--allow-run-as-root", "-np", "1", "python", "mpi_program.py"]
