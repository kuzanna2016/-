print ('Введите слово или фразу кириллицей:')
a = input()
for vowel in 'а','у','е','ы','о','э','я','и','ю','ё':
    a = a.replace(vowel,vowel+'с'+vowel)
print ('Перевод на кирпичный язык:', a)
