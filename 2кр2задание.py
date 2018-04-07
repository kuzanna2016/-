# 2 вариант 2 задание

import re
import collections

with open('mystem.xml', encoding='utf-8') as f:
    mystem = f.read()

gr = re.findall(r'gr="([A-Zа-я0-9,-|()=]+?)"', mystem)

d = collections.Counter(gr)

with open('grcounter.txt','w',encoding='utf-8') as f:
    for key in sorted(d, key=d.get, reverse=True):
        f.write(key+'\n')
