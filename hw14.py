# 3 вариант

import re

def clean_sentences_from_file():
    with open('text.txt', encoding='utf-8') as f:
        text = f.read()
    sentences = re.split(r'[.?!]', text)
    sentences_clean = [re.sub(r'[^\w.!? ]','', sentence) for sentence in sentences]
    return sentences_clean

def word_len(sentences):
    for sentence in sentences:
        words = sentence.split()
        for word in words:
            print('{}_{!s}'.format(word,(len(word))))

word_len(clean_sentences_from_file())

