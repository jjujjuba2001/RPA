from PyPDF2 import PdfReader
path = './SalesKit_website Storyboard_v0.6.4.pdf'
#pdfFile = open('./SalesKit_website Storyboard_v0.6.4.pdf', 'rb')




reader = PdfReader(path)
pages = reader.pages
text = ""
for page in pages:
    sub = page.extract_text()
    text += sub
print(text)