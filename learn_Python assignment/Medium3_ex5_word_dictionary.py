import PyPDF2
import string
import os 

path = os.path.dirname(os.path.abspath(__file__))
file_handle = open(path + '/' + 'Sense-and-Sensibility-by-Jane-Austen.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(file_handle)
page_number = pdfReader.numPages# this tells you total pages

frequency_table = dict()
for page in range(page_number):
    page_object = pdfReader.getPage(page)
    page_text = page_object.extractText()

    #直接判断linel里的word里的每一个element是不是都是letter
    for line in page_text.split('\n'):
        for word in line.split():
            if word != 'CHAPTER':
                letter_list = []
                for letter in word:
                    if letter.isalpha():
                        letter_list.append(letter)
                    else:
                        #没有它，如果word里全是数字，join()函数运行完就会返回''
                        continue
            else:
                continue
            real_word = ''.join(letter_list)
           #method2
           #real_word = ''.join(letter for letter in word if letter.isalpha())

            if real_word in frequency_table:
                frequency_table[real_word] += 1
            else:
                frequency_table[real_word] = 1
    # in the frequency_table exists page_number's invalid 'pages' words
    frequency_table['pages'] = frequency_table['pages'] - page_number

print(frequency_table)