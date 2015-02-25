"""
Given a training vocabulary and a corpus, returns the highest matching documents.
Currently, this is done by purely counting the number of occurrences. An improvement would be to use TfidfVectorizer.
"""

from sklearn.feature_extraction.text import CountVectorizer
import glob
import numpy
import heapq

# Settings
TRAINING = 'todo/concepts_new.txt'
TEST = glob.glob('corpus/*.txt')
N_LARGEST = 5

# Read in vocabulary
vocab = []
with open(TRAINING, 'rb') as f:
    vocab = [l.strip() for l in f.readlines()]

# Start the vectorizer
vectorizer = CountVectorizer(max_df=0.95, min_df=2, input='filename', stop_words='english', vocabulary=vocab)
tfidf = vectorizer.fit_transform(TEST)

# Find the N highest scores
a = numpy.sum(tfidf.todense(), axis=1)
for i in heapq.nlargest(N_LARGEST, range(len(a)), a.take):
    print TEST[i]
