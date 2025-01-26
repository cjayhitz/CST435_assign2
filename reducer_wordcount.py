#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

# Reducer: Sums the counts for each word
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespaces
    word, count = line.split('\t')  # Split the line into word and count
    try:
        count = int(count)
    except ValueError:
        continue  # Skip lines where the count is not an integer

    # If the word is the same as the previous one, add the count to the total
    if current_word == word:
        current_count += count
    else:
        # Output the count for the previous word (if any)
        if current_word is not None:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Output the count for the last word
if current_word is not None:
    print(f"{current_word}\t{current_count}")
