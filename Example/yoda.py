
def master_yoda(text):
    words_split=text.split()
    reverse_sen=words_split[::-1]
    return ' '.join(reverse_sen)

print(master_yoda('I have an apple'))