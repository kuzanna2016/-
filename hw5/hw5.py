<<<<<<< HEAD
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
=======
# 3 вариант
with open("text.txt", encoding="utf-8") as f:
	text = f.read()
nopunct = text.replace(",","").replace(".","").replace(")","").replace("(","").replace("'","").replace("!","").replace("?","").replace(":","").replace(";","").replace("-","").replace('"','')
words = nopunct.split()
one = 0
three = 0
for x in words:
	if len(x) == 1:
		one += 1
	elif len(x) == 3:
		three += 1
if one == 0:
	print("Нет слов длины 1, слов длины 3 - ", three)
else:
	print("Слов длины 3 больше чем слов длины 1 в",round(three/one, 2),"раз")
>>>>>>> origin/master
