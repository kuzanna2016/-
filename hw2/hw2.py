print('Введите слово:')
a = input()
l = len(a)
z = 'з'
r = 'я'
print ('Вывод:')
for i in range(l):
    if a[l-1-i] != z and a[l-1-i] != r:
        print (a[l-1-i])
    
