print ('Введите слово или фразу на английском:')
a = input()
for consonant in 'g','w','r','t','y','p','s','d','f','q','h','j','k','l','z','x','c','v','b','n','m':
    a = a.replace(consonant, consonant+'aig')
print('Перевод на Aigy Paigy:',a)
