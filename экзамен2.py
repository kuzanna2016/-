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

def names():
    upper_all = []
    for file in xml_from_folder():
        with open(file, encoding='utf-8') as f:
            data = f.read()
        upper_all.extend(re.findall(r'lex="([А-ЯЁA-Z]\w*)"', data))
    freq_dict = collections.Counter(upper_all)
    with open ('Names.txt','w', encoding='utf-8') as f:
        for key, value in freq_dict.items():
            f.write('{}\t{}\n'.format(key,value))
    
names()
