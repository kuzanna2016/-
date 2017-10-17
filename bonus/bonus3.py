print ('Введите слово или фразу латиницей:')
a = input()
if a.find(' ') == -1:
    print ('Перевод на Pig Latin:',a[1:]+a[0]+'ay')
else:
    print ('Перевод на Pig Latin:')
    n = a.count(' ')
    for i in range (n):
        space = a.find(' ')
        print (a[1:space]+a[0]+'ay')
        a = a[space+1:]
    print (a[1:]+a[0]+'ay')
