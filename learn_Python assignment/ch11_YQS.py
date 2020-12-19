#ex1.2

text = 'We can know only that we know nothing. And that is the highest degree of human wisdom.'

def histogram_text_words(text):
    """
        Count the number of occurrences of each word in the text，
        text:A string of words
        output：A dictionary of words corresponding to their frequency
    """
    histogram = {}
    words = text.split(" ")
    for c in words:
        if c.isalpha():#Checks if the string consists of only letters
            c = c.lower()
            if c in histogram:
                histogram[c] += 1
            else:
                histogram[c] = 1
        else:
            real_word = ''.join(letter for letter in c if letter.isalpha())

            if real_word in histogram:
                histogram[real_word] += 1
            else:
                histogram[real_word] = 1
    return histogram

dicts = histogram_text_words(text)
for key in dicts:
    print(key,dicts[key],end=' ')


