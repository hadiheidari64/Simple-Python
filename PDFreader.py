#first, make sure PyPDF2 module is intalled > cmd line: #pip3 install PyPDF2
#create a pdf file and put it in the same path of your .py file
# so what this script does, opens the pdf, then reads the pdf using PyPDF2 and anything after that will be most similar to a text file reading
#you can remove pyfiglet module and it is related codes(only used for banner)
#importing required modules
import PyPDF2
import pyfiglet

ascii_banner = pyfiglet.figlet_format("PDF READER")
print(ascii_banner)

# creating a pdf file object
pdfFileObj = open('pypdf.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
