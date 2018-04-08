import re

def yaz_shash(name):
    with open(name, encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'(\W)язы(к[уеиао]?[мвх]?и?)(\W)',
                  r'\1шашлы\2\3',
                  text
                )
    text = re.sub(r'(\W)Язы(к[уеиао]?[мвх]?и?)(\W)',
                  r'\1Шашлы\2\3',
                  text
                )
    with open('Шашлыстика.html', 'w', encoding='utf-8') as f:
        f.write(text)

yaz_shash('Лингвистика.html')
