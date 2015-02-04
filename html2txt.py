from bs4 import BeautifulSoup
import glob

def main():
    files = glob.glob('*.html')

    for f in files: 
        soup = BeautifulSoup(open(f))
        raw = soup.find('div', {'id': 'content'})
        with open(f.split('.')[0] + '.txt', 'w') as o: 
            o.write(raw.text.encode('utf8'))

if __name__ == "__main__":
    main()
    