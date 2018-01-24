# 3 вариант
import random

def noun():
    with open('nouns.txt', encoding='utf-8') as f:
        nouns = f.read()
    nouns = nouns.split(';')
    return random.choice(nouns)

def verb_intransit():
    with open('verbs_intransit.txt', encoding='utf-8') as f:
        verbs_intransit = f.read()
    verbs_intransit = verbs_intransit.split(';')
    return random.choice(verbs_intransit)

def verb_transit_noun_acc():
    with open('verbs_transit.txt', encoding='utf-8') as f:
        verbs_transit = f.read()
    verbs_transit = verbs_transit.split(';')
    with open('nouns_acc.txt', encoding='utf-8') as f:
        nouns_acc = f.read()
    nouns_acc = nouns_acc.split(';')
    
    return random.choice(verbs_transit) + ' ' + random.choice(nouns_acc)

def verb_incentive():
    with open('verbs_incentive.txt', encoding='utf-8') as f:
        verbs_incentive = f.read()
    verbs_incentive = verbs_incentive.split(';')
    return random.choice(verbs_incentive)

def verb_incentive_noun_acc():
    with open('verbs_incentive_transit.txt', encoding='utf-8') as f:
        verbs_incentive_transit = f.read()
    verbs_incentive_transit = verbs_incentive_transit.split(';')
    with open('nouns_acc.txt', encoding='utf-8') as f:
        nouns_acc = f.read()
    nouns_acc = nouns_acc.split(';')
    return random.choice(verbs_incentive_transit) + ' ' + random.choice(nouns_acc)

def question():
    with open('questions.txt', encoding='utf-8') as f:
        questions = f.read()
    questions = questions.split(';')
    return random.choice(questions)

def sentence_declarative():
    return noun().capitalize() + ' ' + random.choice([verb_transit_noun_acc(),verb_intransit()]) + '.'

def sentence_interrogative():
    return question().capitalize() + ' ' + noun() + ' ' + random.choice([verb_transit_noun_acc(),verb_intransit()]) + '?'

def sentence_negative():
    return noun().capitalize() + ' ' + 'не ' + random.choice([verb_transit_noun_acc(),verb_intransit()]) + '.'

def sentence_imperative():
    return noun().capitalize() + ', ' + random.choice([verb_incentive(),verb_incentive_noun_acc()]) + '!'

def sentence_if():
    return 'Если ' + noun() + ' ' + random.choice([verb_transit_noun_acc(),verb_intransit()]) + ', то ' + noun() + ' ' + random.choice([verb_transit_noun_acc(),verb_intransit()]) + '.'

def random_text():
    list_of_sentences = [sentence_declarative(), sentence_interrogative(), sentence_negative(), sentence_imperative(), sentence_if()]
    text = random.sample(list_of_sentences, 5)
    text = ' '.join(text)
    return (text)

print(random_text())
