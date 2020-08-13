import PyPDF2

file_handle =open('Sense-and-Sensibility-by-Jane-Austen.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(file_handle)
page_number = pdfReader.numPages
frequency_table = {}

for i in range(page_number):
    page_object = pdfReader.getPage(i)
    page_text = page_object.extractText()
    for lines in page_text.split('\n'):
        for word in lines.split():
            real_word = ''.join(letter for letter in word if letter.isalpha())
            if real_word in frequency_table:
                frequency_table[real_word] += 1
            else:
                frequency_table[real_word] = 1

print(frequency_table)
