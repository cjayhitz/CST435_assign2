from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def blocking_communication(data):
    start_time = time.time()
    if rank == 0:
        for i in range(1, size):
            comm.send(data, dest=i, tag=11)
    else:
        data_received = comm.recv(source=0, tag=11)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Blocking: Rank {rank} completed in {total_time:.6f} seconds")
    return total_time

def non_blocking_communication(data):
    start_time = time.time()
    if rank == 0:
        requests = []
        for i in range(1, size):
            req = comm.isend(data, dest=i, tag=22)
            requests.append(req)
        MPI.Request.Waitall(requests)
    else:
        req = comm.irecv(source=0, tag=22)
        data_received = req.wait()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Non-blocking: Rank {rank} completed in {total_time:.6f} seconds")
    return total_time

if __name__ == "__main__":
    # Simulate small and large datasets
    if rank == 0:
        small_data = np.random.rand(10)    # Small dataset
        large_data = np.random.rand(10**6) # Large dataset
    else:
        small_data = None
        large_data = None

    # Measure time for blocking and non-blocking with small dataset
    comm.Barrier()
    print("Running blocking communication with small dataset...")
    blocking_time_small = blocking_communication(small_data)

    comm.Barrier()
    print("Running non-blocking communication with small dataset...")
    non_blocking_time_small = non_blocking_communication(small_data)

    # Measure time for blocking and non-blocking with large dataset
    comm.Barrier()
    print("Running blocking communication with large dataset...")
    blocking_time_large = blocking_communication(large_data)

    comm.Barrier()
    print("Running non-blocking communication with large dataset...")
    non_blocking_time_large = non_blocking_communication(large_data)

    # Rank 0 gathers and prints timing summaries
    times = {
        "blocking_small": blocking_time_small,
        "non_blocking_small": non_blocking_time_small,
        "blocking_large": blocking_time_large,
        "non_blocking_large": non_blocking_time_large,
    }
    gathered_times = comm.gather(times, root=0)

    if rank == 0:
        print("\nSummary of Execution Times (seconds):")
        for idx, rank_times in enumerate(gathered_times):
            print(f"Rank {idx}: {rank_times}")
