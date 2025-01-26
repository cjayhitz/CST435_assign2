from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def add_arrays(data_chunk1, data_chunk2):
    """Perform element-wise addition on two data chunks."""
    return data_chunk1 + data_chunk2

if __name__ == "__main__":
    # Problem size: Adjust to 100 million elements
    DATASET_SIZE = 100 * 10**6  # 100 million elements
    CHUNK_SIZE = DATASET_SIZE // size

    start_time = None
    if rank == 0:
        start_time = time.time()  # Start timing at root process
        print(f"Rank {rank} initializing datasets...")

        # Load data (single 1D array)
        data = np.loadtxt('large_dataset.txt')  # Load the dataset

        # Treat the entire dataset as a 1D array
        array1 = data
        array2 = data  # If array1 and array2 are the same, both are set to>
        # Split the arrays into chunks for parallel processing
        chunks1 = [array1[i * CHUNK_SIZE:(i + 1) * CHUNK_SIZE] for i in ran>        chunks2 = [array2[i * CHUNK_SIZE:(i + 1) * CHUNK_SIZE] for i in ran>    else:
        chunks1 = None
        chunks2 = None

    # Scatter chunks to all processes
    data_chunk1 = comm.scatter(chunks1, root=0)
    data_chunk2 = comm.scatter(chunks2, root=0)

    # Perform element-wise addition on the chunks
    result_chunk = add_arrays(data_chunk1, data_chunk2)

    # Gather the results back at the root process
    gathered_results = comm.gather(result_chunk, root=0)

    if rank == 0:
        # Concatenate all gathered chunks into a single result array
        final_result = np.concatenate(gathered_results)
        total_sum = np.sum(final_result)
        end_time = time.time()  # End timing at root process
        elapsed_time = end_time - start_time
        print(f"Rank {rank}: Final sum of the resulting array is {total_sum>        print(f"Rank {rank}: Time taken for the operation: {elapsed_time:.2>
