# 3 вариант
import random

def word_clues_dict():
    with open('words.csv', encoding='utf-8') as f:
        d={}
        for line in f:
            line = line.replace('\n','').replace('\ufeff','')
            word, clue = line.split(';')
            if word in d:
                d[word].append(clue)
            else:
                d[word] = [clue]
    return d

def guess_game():
    print ('Угадайте существительное.')
    print ('У вас будет столько попыток, сколько букв в подсказке.')
    selected_word = random.choice(list(word_clues_dict().keys()))
    selected_clue = random.choice(word_clues_dict()[selected_word])
    print ('Подсказка: ',selected_clue, ' ...')
    attempts = len(selected_clue)
    print ('Количество попыток: ', attempts) 
    user_word = input().lower()
    for i in range(attempts):
        if user_word == selected_word:
            print ('Поздравляем! Вы угадали.')
            break
        elif i == attempts - 1:
            print ('Вы проиграли.')
            break
        else:
            print ('Не подходит. Осталось попыток: ', attempts - 1 - i)
            user_word = input().lower()
    again()
    
def again():
    print ('Если хотите сыграть еще, введите "да"')
    answer = input ().lower()
    if answer == 'да':
        guess_game()

guess_game()
