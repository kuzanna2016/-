# 1 задание
with open('Ozhegov.txt', encoding='utf-8') as f:
    lines=f.readlines()
for line in lines:
    len_word=line.find('|')
    if len_word >= 20:
        print (line)
