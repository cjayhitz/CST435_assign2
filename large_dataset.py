import numpy as np

# Dataset size: 100 million elements
DATASET_SIZE = 100 * 10**6
FILE_NAME = "large_dataset.txt"

# Generate random numbers
data = np.random.rand(DATASET_SIZE)

# Save to a text file, one number per line
with open(FILE_NAME, "w") as f:
    for number in data:
        f.write(f"{number}\n")

print(f"Dataset of size {DATASET_SIZE} saved to {FILE_NAME}.")
