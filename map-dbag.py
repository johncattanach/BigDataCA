#!/usr/bin/env python
# map-dbag.py
# map incoming csv into word,mbti type tuples
# nb using pandas dataframe for prototyping purposes
import sys
import re
import pandas as pd
from nltk.stem import WordNetLemmatizer
# do these one time
#import nltk
#nltk.download('wordnet')
#nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

def validword(s):    
    if s.isascii():  # ignore emtocicon and non-english text
        # ignore url/handle/3 or more key mashing
        if re.match(r'^http|^@|(.)\1{2,}',s):
            return ''
        # only allow letters
        elif re.match(r'^[a-zA-Z]*$',s):
            return lemmatizer.lemmatize(s.lower())
        else:
            return ''
    else:
        return ''
# replace stdin for development
df = pd.read_csv(sys.stdin)
#df = pd.read_csv('twitter_MBTI.csv')
# Iterate over each row in the csv
# file using reader object
# NB in production would replace with a streaming equivalent
# each row is one person, so have that as a fixed length number
# (fixed length so it sorts ok)
d=1
for i,row in df.iterrows():
    d=d+1
    for tweet in row['text'].split('|||'):
        for word in tweet.split():
            # ignore urls and handles
            w=validword(word)
            if w != '':
                print(f'{d:010}.{row["label"]}.{w}\t1')
