# WIP Python file to search words and patterns. Runs with python 2.6, as PyPDF2 is not compatible with newer Python versions.

import os
import PyPDF2 as runpdf
filename=input('\nFilename:')
pdf_file = open(filename,"rb")
pdf_reader = runpdf.PdfFileReader(pdf_file)
filename=raw_input('\nFilename:')

pdfFile = PdfFileReader(pdf_file)
if pdfFile.isEncrypted:
    try:
        pdfFile.decrypt('')
        print ("File Decrypted (PyPDF2)")
    except:
        command="cp "+filename+" temp.pdf; qpdf --password='' --decrypt temp.pdf "+filename
        os.system(command)
        print ('File Decrypted (qpdf)')
        #re-open the decrypted file
        pdf_file = open(filename)
        pdfFile = PdfFileReader(pdf_file)
else:
    print ('File Not Encrypted')
#dostuff with pdfFile here



page = pdf_reader.getPage(1)
cargado = pageObj.extractText()

print(cargado)


