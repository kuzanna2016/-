# 3 вариант
print('Ведите слово:')
word=input()
if word == '':
	print('Ничего не введено')
for i in range(len(word)-1):
	word = word[1:]+word[0]
	print(word)
