"""
Modified from http://scikit-learn.org/stable/auto_examples/document_clustering.html
Original Authors: 
- Olivier Grisel <olivier.grisel@ensta.org>
- Lars Buitinck <L.J.Buitinck@uva.nl>
License: 
- BSD 3 clause
"""

from __future__ import print_function
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from time import time
import glob
import os
import csv
import matplotlib.pyplot as plt

# Load the dataset
t0 = time()
print("Loading dataset and extracting TF-IDF features...")
files = glob.glob('corpus/*.txt')

# Calculate tf-idf scores.
# - max_df: maximum percentage of documents that can have this term
#   (so terms that occur in more than 95% of the corpus are ignored)
# - min_df: minimum amount of times word should occur in the corpus
#   (so terms that occur in less than 2 documents of the corpus are ignored)
vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, input='filename', stop_words='english')
tfidf = vectorizer.fit_transform(files)

print("done in %0.3fs." % (time() - t0))

# Perform K-means clustering for a number of clusters
# Inertia is saved to be able to plot this on a graph later
x = []
y = []
for n_clusters in range(2, 21):
    t0 = time()
    km = KMeans(n_clusters=n_clusters)
    km.fit(tfidf)
    print("done in %0.3fs." % (time() - t0))

    # Write top terms per cluster to a .txt-file
    with open('clusters' + str(n_clusters) + '.txt', 'wb') as c_file:
        order_centroids = km.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names()
        for i in range(n_clusters):
            c_file.write('Cluster %d:' % i)
            for ind in order_centroids[i, :10]:
                c_file.write(' %s' % terms[ind].encode('utf-8'))
            c_file.write('\n')

    # Write files and their clusters to .csv-file
    with open('clusters' + str(n_clusters) + '.csv', 'wb') as c_file:
        c_writer = csv.writer(c_file)
        c_writer.writerow(['filename', 'cluster'])
        for n, f in enumerate(files):
            c_writer.writerow([os.path.basename(f), km.labels_[n]])

    # Save the inertia for this cluster
    x.append(n_clusters)
    y.append(km.inertia_)

# Plots the inertia per number of clusters
plt.plot(x, y, 'ob-')
plt.show()