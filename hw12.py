# 3 вариант

import os
import re

def cyrillic_folder_list():
    file_list = os.listdir()
    folder_list = []

    for file in file_list:
        file_path = os.path.join('.', file)
        if os.path.isdir(file_path):
            if re.search(r'[^А-Яа-яё]', file) == None: #если в задании считается, что только кириллические символы, даже без знаков препинания, пробелов и цифр
                folder_list.append(file)
    return folder_list

def result(folder_list):
    if len(folder_list) == 0:
        print('Папок с кириллицей нет')
    else:
        print('Количество папок, названия которых состоят из кириллических символов:', len(folder_list))
        print('Эти папки:')
        for folder in folder_list:
            print(folder)

result(cyrillic_folder_list())
