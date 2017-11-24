# 3 вариант
with open('text.txt', 'w', encoding='utf-8') as f:
        f.write('')

print('Вводите слова через ENTER. Когда вы закончите, введите пустую строку.')
word = input()

if word == '':
    print('Ни одного слова не было введено.')
    
count = 0
while word != '':
    count += 1
    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write(word[count:]+'\n')
    word = input()
