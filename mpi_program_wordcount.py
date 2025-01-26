from mpi4py import MPI
import os

def count_words_in_file(file_name):
    word_count = {}
    with open(file_name, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.strip().lower()
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1
    return word_count

def mpi_wordcount():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        # Root process: distribute files to workers
        file_names = ["file1.txt", "file2.txt", "file3.txt"]  # Example file names
        chunks = [file_names[i::size] for i in range(size)]
    else:
        chunks = None

    # Scatter the chunks of files to each worker
    chunk = comm.scatter(chunks, root=0)
    
    # Each process counts words in its assigned files
    word_count = {}
    for file_name in chunk:
        word_count.update(count_words_in_file(file_name))
    
    # Gather all word counts at the root process
    all_word_counts = comm.gather(word_count, root=0)
    
    if rank == 0:
        final_word_count = {}
        for wc in all_word_counts:
            for word, count in wc.items():
                if word in final_word_count:
                    final_word_count[word] += count
                else:
                    final_word_count[word] = count
        print(final_word_count)

if __name__ == "__main__":
    mpi_wordcount()
