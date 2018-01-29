#3 вариант
import collections

def from_file_to_words(name):
    with open(name, encoding='utf-8') as f:
        text = f.read()
    for i in ['.',',','?','!',';',':','"','- ','-','—','(',')',"'",'”','’']: # в тексте Остин есть опечатки, от них можно только искусственно избавиться
        text = text.replace(i,'')
    text = text.lower()
    words = text.split()
    return words

def hood_list(name):
    hood_list = []
    for word in from_file_to_words(name):
        hood = word.find('hood')
        _hood = word[:hood]
        if hood != -1 and _hood != '': #чтобы не считать слова, где hood не суффикс
            if word.find('hoods') != -1: #чтобы не считать множественное число или слово с притяжательным 's\s' другим словом
                word = word[:-1]
            
            hood_list.append(word)
    return hood_list

def hood_min_freq(name):
    hood_freq = collections.Counter(hood_list(name))
    hood_min_freq = sorted(hood_freq.values())[0]
    hood_min = ''
    for key, value in hood_freq.items():
        if value == hood_min_freq:
            hood_min += key + ', '
    hood_min = hood_min[:-2]
    print ('Существительные с наименьшей частотностью (', hood_min_freq,'): ', hood_min)

def hood_dict(name):
    hood_dict = {}
    for word in hood_list(name):
        _hood = word[:word.find('hood')]
        hood_dict[word] = _hood
    return hood_dict

def hood_deriv (name):
    hood_deriv = ''
    for value in hood_dict(name).values():
        hood_deriv += value + ', '
    hood_deriv = hood_deriv[:-2]
    print ('Слова от которых образованы: ', hood_deriv)

def hood_article(name):
    print ('В тексте ', len(hood_list(name)), ' существительных с суффиксом -hood.')
    hood_min_freq(name)
    hood_deriv(name)

hood_article(input('Введите название файла: '))
