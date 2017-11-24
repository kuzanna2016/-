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
	print("Слов длины 3 больше чем слов длины 1 в",round(three/one, 2),"раз"
