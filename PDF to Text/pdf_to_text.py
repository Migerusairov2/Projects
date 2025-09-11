import PyPDF2

with open('pdf/TV_TEST.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0]
    text = page.extract_text(1)
    print(text)
