from __future__ import division
from sklearn.feature_extraction.text import TfidfVectorizer

import glob
import numpy as np
import nltk
import string

class Similarity: 
    """Calculates the similarity of a set of files"""
    files = set()

    def __init__(self, files):
        self.files = files

    def tokenize(self, text):
        """Tokenizes, removes punctuation and stems the given text.""" 
        words = nltk.word_tokenize(text)
        tokens = filter(lambda w: w not in string.punctuation, words)
        stemmer = nltk.stem.snowball.EnglishStemmer()
        #stemmer = nltk.stem.porter.PorterStemmer() # Alternative stemmer
        return [stemmer.stem(t) for t in tokens]

    def pairwise_similarity(self): 
        """
        Returns the cosine similarity of a set of files.
        Idea from http://stackoverflow.com/a/8897648/3710392
        """
        vectorizer = TfidfVectorizer(input='filename', tokenizer=self.tokenize, stop_words='english')
        tfidf = vectorizer.fit_transform(self.files)
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
