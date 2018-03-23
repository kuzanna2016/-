#3 вариант

import re
import collections

def from_file_to_text(name):
    while name == '':
        print('Ничего не введено')
        name = input('Введите название файла с русским текстом в кодировке utf-8:')
    with open(name, encoding='utf-8') as f:
        text = f.read()
        for i in ['.',',','?','!',';',':','"','- ','-','—','(',')',"'",'”','’']:
            text = text.replace(i,' ')
    return text


def forms_finder(text):
    forms = []
    words = []
    #я не знаю как сделать это красиво, цикл тоже громоздкий будет
    forms.append('[Пп]рограммиру[ею][мтш]?[еь]?с?[яь]?\s')
    forms.append('[Пп]рограммиру[йя](?:те)?с?[яь]?\s')
    forms.append('[Пп]рограммирующ[иаеу][йхгмяюеи][оу]?с?[яь]?\s')
    forms.append('[Пп]рограммируем[ыаоу][йхгмяюеи][оу]?с?[яь]?\s')
    forms.append('[Пп]рограммировал[аои]?с?[яь]?\s')
    forms.append('[Пп]рограммировав[шщ]?[иаеу]?[йхгмяюеи][оу]?с?[яь]?\s')
    forms.append('[Бб]уд[уе]?[тмш]?[ье]? программировать(?:ся)?\s')
    forms.append('[Пп]рограммировать(?:ся)?\s')

    for form in forms:
        words.extend(re.findall(form, text))
        
    counter = collections.Counter(words)
    print('Формы глагола "программировать", которые встретились в тексте:')
    for word in counter:
        print(word)

forms_finder(from_file_to_text(input('Введите название файла с русским текстом в кодировке utf-8:')))

