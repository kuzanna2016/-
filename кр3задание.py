# 3 задание
with open('Ozhegov.txt', encoding='utf-8') as f:
    lines=f.readlines()

print('Вводите слова через ENTER. Когда вы закончите, введите пустую строку.')
word = input()

if word == '':
    print('Ни одного слова не было введено.')

while word != '':
    found = 0
    for line in lines:
        line_parts=line.split('|')
        
        if line_parts[3] == '\n':
            line_parts[3] = 'нет употребления'
        else:
            line_parts[3] = line_parts[3].replace('\n','')
            
        if word == line_parts[0]:
            found = 1
            description = word +'-'+line_parts[3]+'-'+line_parts[1]
            print(description)
            
    if found == 0:
        print('Слово не нашлось')
    word = input()
