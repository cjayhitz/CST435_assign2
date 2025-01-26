#!/usr/bin/env python3
import sys

current_sum = 0
current_key = None

# Reducer: Sums the numbers for each key (in this case, the same number)
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespaces
    key, value = line.split('\t')  # Split the line into key and value
    try:
        key = int(key)
        value = int(value)
    except ValueError:
        continue  # Skip lines where conversion fails
    
    # If the key is the same as the previous one, add the value to the sum
    if current_key == key:
        current_sum += value
    else:
        # Output the sum for the previous key (if any)
        if current_key is not None:
            print(f"{current_key}\t{current_sum}")
        current_key = key
        current_sum = value

# Output the sum for the last key
if current_key is not None:
    print(f"{current_key}\t{current_sum}")
