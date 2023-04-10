#!/usr/bin/env python
# map-bag.py
# map incoming csv into word,mbti type tuples
# nb using pandas dataframe for prototyping purposes
import sys
import re
import pandas as pd
def validword(s):    
    if s.isascii():  # ignore emtocicon and non-english text
        if re.match(r'^http|^@',s):
            return ''
        else:
            return s.lower()
    else:
        return ''
# replace stdin for development
df = pd.read_csv(sys.stdin)
# Iterate over each row in the csv
# file using reader object
# NB in production would replace with a streaming equivalent
for i,row in df.iterrows():
    for tweet in row['text'].split('|||'):
        for word in tweet.split():
            # ignore urls and handles
            w=validword(word)
            if w != '':
                print(f'{w}\t{row["label"]}\t1')
