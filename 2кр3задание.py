# 2 вариант 3 задание

import re

with open('mystem.xml', encoding='utf-8') as f:
    mystem = f.read()

verbs = re.findall(r'gr="(V[,=][а-я0-9,-|()=]*?)"', mystem)
perfverb = []
for verb in verbs:
    if re.search(r',сов', verb) != None and re.search(r'мн', verb)!= None:
        perfverb.append(verb)

with open('verbperf.txt','w',encoding='utf-8') as f:
    f.write(str(len(perfverb)))

#лемма разбор словоформа

mystem = mystem.splitlines()
with open('mystem.csv','w',encoding='utf-8') as f:
    for line in mystem:
        csv = re.search(r'<w><ana lex="(\w+?)" gr="([а-я0-9,-|()=]*?)" />(\w+?)</w>', line)
        if csv != None:
            f.write(csv.group(1)+','+re.sub(r',',r'',csv.group(2))+','+csv.group(3)+'\n')
