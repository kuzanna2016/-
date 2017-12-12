# 2 задание
with open('Ozhegov.txt', encoding='utf-8') as f:
    lines=f.readlines()
antonyms = 0
for line in lines:
        line_parts=line.split('|')
        if line_parts[2] != '':
            antonyms += 1
print ('Количесвто слов с антонимами -', antonyms)
