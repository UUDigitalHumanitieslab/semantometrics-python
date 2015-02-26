# semantometrics-python

*semantometrics-python* is a Python toolset that tries to mimic the semantometrics research contribution measure, 
as being described by Petr Knoth and Drahomira Herrmannova in their 
[2014 article](http://www.dlib.org/dlib/november14/knoth/11knoth.html). 
This repository contains tools for calculating this and other measures, 
as well as preprocessing scripts to get from .html/.pdf to .txt-files.   

## Preprocessing 

### PDF to text

* **File:** 
*pdf2txt.py*
* **Usage:** 
Just move the script to a folder with .pdf-files and run it. It will output .txt-files.  
* **Packages used:** 
To get from PDF files (the de facto standard for research papers) to plain text files, 
we use the [PDFMiner](https://euske.github.io/pdfminer/) package. 
An alternative would be the Java package [Apache Tika](http://tika.apache.org), 
which is actually used by Knoth and Herrmanova.

### HTML to text

* **Files:** 
*html2txt_cultmach.py*, 
*html2txt_theoryandevent.py*
* **Usage:** 
Just move the script to a folder with .html-files and run it. It will output .txt-files. 
* **Packages used:** 
To get from HTML files to plain text files, we use the [BeautifulSoup](https://euske.github.io/pdfminer/) package.
The HTML format is used by a few research papers, usually with different lay-out (YMMV), 
that's why there are a few of these converters in the repository.   
Currently supported journals: 
    - [Culture Machine](http://www.culturemachine.net/)
    - [Theory and Event](http://muse.jhu.edu/journals/theory_and_event/)

## Tools

### Semantic Similarity

* **File:** 
*semantometrics.py*
* **Usage:** 
The script is set up to work with two sets of files: references of the research article in question 
(A-set, .txt-files starting with the letter 'a') and citations of the research article 
(B-set, .txt-files starting with the letter 'b'). The script expects these files to be in the same directory. 
The script returns the result of the contribution function defined by Knoth and Herrmannova.
* **Packages used:** 
For tf-idf calculation (the measure used in Knoth and Herrmannova's article) we use the 
[scikit-learn](http://scikit-learn.org/) implementation with a modified tokenization: 
[NLTK](http://www.nltk.org/)'s implementation of the [Porter2 (Snowball) stemmer](http://snowball.tartarus.org/). 
We also opted to remove punctuation and tokens that contain digits (e.g. '1987' and 'a2c').  

### Gephi output

* **File:** 
*gephi_input.py*
* **Usage:** 
We can also use tf-idf to calculate semantic similarity between files instead of sets of files. 
We can then use this measure (called *cosine similiarity*) as weights on an undirected graph. 
This allows us to do all sorts of cluster analysis with tools like [Gephi](http://gephi.github.io/). 
The script creates two input files for Gephi: 
    - *nodes.csv*, which contains the nodes of the network 
    - *edges.csv*, which contains the weighted edges of the network. 
* **Packages used:** 
We use the same measure of similarity as in the above semantic similarity tool. 

### Topic extraction 

* **File:** 
*topic_extraction.py*
* **Usage:** 
This script can be used to generate clusters from a corpus based on semantic similarity. 
The script uses [*k*-means clustering](http://en.wikipedia.org/wiki/K-means_clustering). 
Per cluster, the top terms can be identified, which makes it a bit more insightful than the clustering with Gephi above. 
The script creates two output files per *k* number of clusters: 
    - *clusters<k>.txt*, which contains the top terms per cluster
    - *clusters<k>.csv*, which contains the cluster association for each input file. 
Also, a graph is plotted with the inertia per *k* number of clusters, so that a value for *k* can be chosen
with the [elbow method](http://en.wikipedia.org/wiki/Determining_the_number_of_clusters_in_a_data_set#The_Elbow_Method).
* **Packages used:** 
The script uses the [scikit-learn](http://scikit-learn.org/) implementation of K-means clustering, 
and again the tf-idf calculation from the same package, this time with the built-in tokenization. 
For the most part, the script is adapted from 
[an example on the scikit-learn website](http://scikit-learn.org/stable/auto_examples/document_clustering.html) 
to which the looping over *k*, the output files and the plotting of the inertia were added.  
To plot the inertia, the script uses [matplotlib](http://matplotlib.org/). 

### Corpus counting

* **File:** 
*corpus_count.py*
* **Usage:** 
This script can be used to count the number of occurrences of a certain list of words in a corpus. 
* **Packages used:** 
The script uses the [scikit-learn](http://scikit-learn.org/) implementation of word counting. 
