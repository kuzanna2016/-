import xml.etree.ElementTree as ET
import re
import os
import collections

def xml_from_folder():
    file_list = os.listdir()
    xml_list = []
    for file in file_list:
        if re.search("\.", file) != None:
            name, ext = file.split('.')
        if ext == 'html':
            xml_list.append(file)
    return xml_list

#with open ('clean.txt', 'w', encoding='utf-8') as f:
#    f.write('')
#for file in xml_from_folder():
#        with open(file, encoding='utf-8') as f:
#            data = f.read()
#        clean = re.sub(r'<.*?>',r'', data).replace('`','')
#        clean = re.sub(r'(\w) \.',r'\1.', clean)
#        #clean = re.sub(r'(\W)\n', '\1', clean)
#        with open ('clean.txt', 'a', encoding='utf-8') as f:
#            f.write(clean)
            
def get_tree(url):
    with open(url, encoding='utf-8') as f:
        root = ET.fromstring(f.read())
    return root


with open ('clean.txt', 'w', encoding='utf-8') as f:
    f.write('')
for file in xml_from_folder():
    for sentence in get_tree(file)[1]:
            sentence_string = ''
            for word in sentence:
                for ana in word:
                    if ana.tail != None and word.tail != None:
                        merge = ana.tail + word.tail.replace('\n', '')
                        sentence_string += merge + ' '
            with open ('clean.txt', 'a', encoding='utf-8') as f:
                f.write(get_tree(file)[0][0].text)
                f.write(sentence_string.replace('`',''))
