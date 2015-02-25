from bs4 import BeautifulSoup
import glob
import os


# Transforms a set of .html-files into .txt.
def main():
    files = glob.glob('corpus/TheoryandEvent/TheoryandEventVol182014/*.html')

    for f in files: 
        soup = BeautifulSoup(open(f))
        raw = soup.find('div', {'id': 'body'})
        print os.path.basename(f)
        with open(os.path.basename(f) + '.txt', 'w') as o:
            o.write(raw.text.replace('\t', '').encode('utf8'))

if __name__ == "__main__":
    main()
