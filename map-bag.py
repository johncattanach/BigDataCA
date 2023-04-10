#!/usr/bin/env python
import sys
import re
import pandas as pd
def validword(s):
    if re.match(r'^http|^@',s):
        return 'x'
    else:
        return s.lower()
# imitate stdin
with open('twitter_MBTI.csv') as f:
    df = pd.read_csv(sys.stdin)
    # Iterate over each row in the csv
    # file using reader object
    #df.info()
    for i,row in df.iterrows():
        for tweet in row['text'].split('|||'):
            for word in tweet.split():
                # ignore urls and handles
                w=validword(word)
                if w != '':
                    print(f'{w}\t1')
