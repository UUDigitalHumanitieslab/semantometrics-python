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

* **File:** 
*html2txt_cultmach.py*
*html2txt_theoryandevent.py*
* **Usage:** 
Just move the script to a folder with .html-files and run it. It will output .txt-files. 
* **Packages used:** 
To get from HTML files to plain text files, we use the [BeautifulSoup](https://euske.github.io/pdfminer/) package.
The HTML format is used by a few research papers, usually with different formats (YMMV), 
that's why there are a few of these files in the repository. 

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
This tool creates two .csv-files to be read in with [Gephi](http://gephi.github.io/). 
* **Packages used:** 
We use the same measure of similarity as in the above semantic similarity tool. 

### Topic extraction 

* **File:** 
*topic_extraction.py*
* **Usage:** 
TODO
* **Packages used:** 
TODO

### Corpus counting

* **File:** 
*corpus_count.py*
* **Usage:** 
TODO
* **Packages used:** 
TODO
