from __future__ import division
from sklearn.feature_extraction.text import TfidfVectorizer

import glob
import numpy as np
import nltk
import string

def main(): 
    """Retrieves the files and calculates the Contribution score."""
    a_files = glob.glob('a*.txt')
    b_files = glob.glob('b*.txt')

    a = pairwise_distance(b_files) / pairwise_distance(a_files)
    b = 1 / (len(a_files) * len(b_files))
    c = distance_sum(pairwise_similarity(a_files + b_files))

    #print a, b, c, a * b * c
    print a * b * c

def tokenize(text):
    """Tokenizes, removes punctuation and stems the given text.""" 
    words = nltk.word_tokenize(text)
    tokens = filter(lambda w: w not in string.punctuation, words)
    stemmer = nltk.stem.snowball.EnglishStemmer()
    #stemmer = nltk.stem.porter.PorterStemmer() # Alternative stemmer
    return [stemmer.stem(t) for t in tokens]

def pairwise_similarity(files): 
    """
    Returns the cosine similarity of a set of files.
    Copied (mostly) from http://stackoverflow.com/a/8897648/3710392
    """
    documents = list()
    for f in files: 
        with open(f, 'r') as doc: 
            r = doc.read()
            documents.append(r)
            #print tokenize(r.decode('utf-8'))

    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english').fit_transform(documents)
    return (tfidf * tfidf.T).A
    # retrieving a specific value: print ((tfidf * tfidf.T).A)[0,1]

def distance_sum(matrix):
    """Returns the total sum of 1 - matrix, minus the main diagonal."""
    matrix = 1 - matrix
    np.fill_diagonal(matrix, 0)
    return matrix.sum()

def pairwise_distance(files):
    """Returns the pairwise distance (cosine similarity normalized)."""
    l = len(files)
    if l == 1: 
        return 1
    else: 
        ps = pairwise_similarity(files)
        return (1 / (l * (l - 1))) * distance_sum(ps)

if __name__ == "__main__":
    main()
