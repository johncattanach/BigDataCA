#!/usr/bin/env python

import sys

curr_word = None
curr_label=None
curr_count = 0

# Process each key-value pair from the mapper
for line in sys.stdin:

  # Get the key and value from the current line
  word_label,count = line.split('\t')

  # Convert the count to an int
  count = int(count)

  # split word_label pair
  word,label=word_label.split('.')
  # If the current word is the same as the previous word, 
  # increment its count, otherwise print the words count 
  # to stdout
  if word == curr_word and label == curr_label:
     curr_count += count
  else:

     # Write word,label and its number of occurrences as a key-value 
     # pair to stdout
     if curr_word:
        print (f'{curr_word}\t{curr_label}\t{curr_count}')

     curr_word = word
     curr_label=label
     curr_count = count

# Output the count for the last word
if curr_word == word and curr_label==label:
  print (f'{curr_word}\t{curr_label}\t{curr_count}')
