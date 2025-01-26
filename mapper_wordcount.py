#!/usr/bin/env python3
import sys

# Mapper: Reads data line by line, emits each word as a key-value pair
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespaces
    words = line.split()  # Split the line into words
    for word in words:
        # Emit the word and a count of 1
        print(f"{word}\t1")
