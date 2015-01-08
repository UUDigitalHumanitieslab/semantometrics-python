# Semantometrics

Semantometrics is a Python script that tries to mimic the semantometrics research contribution measure, as being described by Petr Knoth and Drahomira Herrmannova in their [2014 article](http://www.dlib.org/dlib/november14/knoth/11knoth.html). 

## PDF to text

To get from PDF files (the de facto standard for research papers) to plain text files, we used the [PDFMiner](https://euske.github.io/pdfminer/) package without modifications. An alternative would be [Apache Tika](http://tika.apache.org/). 

## Semantic Similarity

For tf-idf calculation (the measure used in Knuth and Herrmannova's article) we use the [scikit-learn](http://scikit-learn.org/) implementation with a modified tokenization: [NLTK](http://www.nltk.org/)'s implementation of the [Porter2 (Snowball) stemmer](http://snowball.tartarus.org/). We also opted to remove punctuation. 

# Usage 

Currently, the script is set up to work with two sets of files: references of the research article in question (A-set, .txt-files starting with the letter 'a') and citations of the research article (B-set, .txt-files starting with the letter 'b'). The script expects these files to be in the same directory. The script returns the result of the contribution function defined by Knuth and Herrmannova.
