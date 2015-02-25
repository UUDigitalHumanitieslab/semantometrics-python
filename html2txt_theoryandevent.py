from bs4 import BeautifulSoup
import glob
import os

CORPUS_DIR = 'corpus/TheoryandEvent/'

# Transforms a set of .html-files into .txt.
def main():
    for _, subdirs, _ in os.walk(CORPUS_DIR):
        for subdir in subdirs:
            print subdir
            files = glob.glob(CORPUS_DIR + subdir + '/*.html')
            year = int(subdir[-4:])
            if year <= 2007:
                extract_old(files)
            else:
                extract_new(files)


def extract_old(files):
    for f in files:
        soup = BeautifulSoup(open(f))
        body = soup.find('body')

        with open(f.replace('.html', '.txt'), 'w') as o:
            o.write(body.text.replace('\t', '').encode('utf8'))


def extract_new(files):
    for f in files: 
        soup = BeautifulSoup(open(f))
        title = soup.find('div', {'id': 'article-title'})  # TODO: subtitle, e.g. 12.4.plot.html
        authors = soup.find('div', {'class': 'contrib'})  # TODO: remove bio link
        body = soup.find('div', {'id': 'body'})
        notes = soup.find('div', {'class': 'fn-group'})

        with open(f.replace('.html', '.txt'), 'w') as o:
            if title:
                o.write(title.text.encode('utf8'))
            if authors:
                o.write(authors.text.encode('utf8'))
            if body:
                o.write(body.text.replace('\t', '').encode('utf8'))
            if notes:
                o.write(notes.text.encode('utf8'))

if __name__ == "__main__":
    main()
