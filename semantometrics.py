from __future__ import division
from sklearn.feature_extraction.text import TfidfVectorizer

import glob
import numpy as np
import nltk
import string
import re


class Similarity: 
    """Calculates the similarity of a set of files"""
    files = set()
    vectorizer = TfidfVectorizer()

    def __init__(self, files):
        self.files = files

    def pairwise_similarity(self):
        """
        Returns the cosine similarity of a set of files.
        Idea from http://stackoverflow.com/a/8897648/3710392
        """
        self.vectorizer = TfidfVectorizer(input='filename', tokenizer=tokenize, stop_words='english')
        tfidf = self.vectorizer.fit_transform(self.files)
        return (tfidf * tfidf.T).A
        # retrieving a specific value: print ((tfidf * tfidf.T).A)[0,1]

    def pairwise_distance(self):
        """Returns the pairwise distance (cosine similarity normalized)."""
        l = len(self.files)
        if l == 1: 
            return 1
        else: 
            ps = self.pairwise_similarity()
            return (1 / (l * (l - 1))) * distance_sum(ps)

    def print_vocabulary(self): 
        """Prints the vocabulary to a file"""
        f = open('vocab.txt', 'w')
        for v in self.vectorizer.vocabulary_: 
            f.write(v.encode('utf-8') + '\n')


def tokenize(text):
    """Tokenizes, removes punctuation and stems the given text."""
    tokens = nltk.word_tokenize(text)
    tokens = remove_punctuation(tokens)
    tokens = remove_digits(tokens)
    stemmer = nltk.stem.snowball.EnglishStemmer()
    #stemmer = nltk.stem.porter.PorterStemmer() # Alternative stemmer
    t = [stemmer.stem(t) for t in tokens]
    return t


def remove_punctuation(tokens):
    """
    Removes any punctuation from a list of tokens
    >>> remove_punctuation(['abc', ':', 'def', ';'])
    ['abc', 'def']
    """
    return filter(lambda t: t not in string.punctuation, tokens)


def remove_digits(tokens):
    """
    Removes any token having a digit from a list of tokens
    >>> remove_digits(['abc', 'a2c', '1987'])
    ['abc']
    """
    return filter(lambda t: not re.search(r'\d', t), tokens)


def distance_sum(matrix):
    """Returns the total sum of 1 - matrix, minus the main diagonal.
    >>> print distance_sum(np.matrix('1 .2 .3; .4 1 .5; .6 .7 1'))
    3.3
    """
    matrix = 1 - matrix
    np.fill_diagonal(matrix, 0)
    return matrix.sum()


def main(): 
    """Retrieves the files and calculates the Contribution score."""
    a_files = glob.glob('dataset/sample/a*.txt')
    b_files = glob.glob('dataset/sample/b*.txt')

    # Create Similarity objects
    s_a = Similarity(a_files)
    s_b = Similarity(b_files)
    s_ab = Similarity(a_files + b_files)

    # Calculate the parts of the Contribution score
    a = s_b.pairwise_distance() / s_a.pairwise_distance()
    b = 1 / (len(a_files) * len(b_files))
    c = distance_sum(s_ab.pairwise_similarity())

    print a * b * c

if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
