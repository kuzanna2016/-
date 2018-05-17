# 3 вариант

import os
import collections
import re

# я не поняла условие, поэтому функция ниже для всех папок сразу
def freq_ext_all():
    ext_list = []
    start = '.'
    for root, dirs, files in os.walk(start):
        for file in files:
            if re.search("\.", file) == None:
                ext_list.append("no extension")
            else:
                name, ext = file.split(".")
                ext_list.append(ext)
    freq_ext = collections.Counter(ext_list)
    for ext in sorted(freq_ext, key=freq_ext.get, reverse=True):
        print("В папках, где находится программа чаще всего встречаются файлы с расширением", "'" + ext + "'")
        break

# эта функция для каждой папки поочереди
def freq_ext_every():
    ext_list = []
    start = '.'
    for root, dirs, files in os.walk(start):
        for file in files:
            if re.search("\.", file) == None:
                ext_list.append("no extension")
            else:
                name, ext = file.split(".")
                ext_list.append(ext)
        freq_ext = collections.Counter(ext_list)
        for ext in sorted(freq_ext, key=freq_ext.get, reverse=True):
                print("В папке", "'" + os.path.split(root)[1] + "'", "чаще всего встречаются файлы с расширением", "'" + ext + "'")
                break
        ext_list = []
    
freq_ext_all()
freq_ext_every()

