import xml.etree.ElementTree as ET
import os
import re

def get_tree(url):
    with open(url, encoding='utf-8') as f:
        root = ET.fromstring(f.read())
    return root

def xml_from_folder():
    file_list = os.listdir()
    xml_list = []
    for file in file_list:
        if re.search("\.", file) != None:
            name, ext = file.split('.')
        if ext == 'html':
            xml_list.append(file)
    return xml_list
 
 
def get_part_of_speech_with_attr(data):
 
    table = []
    for sentence in data[1]:
        sentence_string = ''
        for word in sentence:
            for ana in word:
                if ana.tail != None:
                    merge = ana.tail + word.tail
                    sentence_string += merge.replace('\n', '') + ' '
 
        for i in range(len(sentence) - 1):
            a = sentence[i][0].attrib['gr']
            b = sentence[i + 1][0].attrib['gr']
            grammar_a = a.replace('=', ',').split(',')
            grammar_b = b.replace('=', ',').split(',')
 
            if grammar_a[0] == 'NUM':
                print('+')
                if grammar_b[0] == 'S' and 'gen' in grammar_b:
                    s = sentence[i][0].tail + ' ' +sentence[i+1][0].tail
                    table.append([s, sentence_string, sentence])
 
    return table
 
def meta_dict(data):
    meta_dict = dict()
    for meta in data[0][1:]:
        meta_dict[meta.attrib['name']] = meta.attrib['content']
    return meta_dict
 
data = get_tree('rian1.html')
bits_list = get_part_of_speech_with_attr(data)
print(bits_list)

def num_csv(file):
    with open ('num.csv', 'a') as f:
        for bigram in get_part_of_speech_with_attr(get_tree(file)):
            for s in bigram:
                f.write(meta_dict(get_tree(file))['docid']+';'+s+';'+meta_dict(get_tree(file))['topic']+'\n')

with open ('num.csv', 'w') as f:
        f.write('doc_id;найденая биграмма;topic\n')
num_csv('rian1.html')
