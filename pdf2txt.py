import subprocess
import glob

# Transforms a set of .pdf-files into .txt. 
# Uses the pdf2txt.py script from PDFMiner: https://github.com/euske/pdfminer
for f in glob.glob('*.pdf'):
    text_file = f.split('.')[0] + '.txt'
    subprocess.call(['python', 'C:\Python27\Scripts\pdf2txt.py', '-o', text_file, f])