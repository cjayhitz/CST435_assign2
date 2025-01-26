#!/usr/bin/env python3
import sys

# Mapper: Reads data line by line, emits each number as a key-value pair
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespaces
    try:
        # Assuming the elements are integers, convert the line to int
        number = int(line)
        print(f"{number}\t1")  # Emit the number and a count of 1
    except ValueError:
        continue  # Ignore lines that don't represent integers
