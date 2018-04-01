# 3 вариант

import re

def open_html(name):
    while name == '':
        print('Ничего не введено')
        name = input('Введите название html-файла с русским текстом в кодировке utf-8:')
    with open(name, encoding='utf-8') as f:
        html = f.read()
    return html

def search_year(html):
    name = re.search(r'<h1 id="firstHeading" class="firstHeading" lang="ru">(.*?)</h1>', html)
    year = re.search(r'data-wikidata-property-id="P571">.*?([12]\d\d\d).*?</span>', # болонский университет основан в 1088 - самый старый университет мира
        html
    )
    print(name.group(1) + '.','Год основания -', year.group(1))

search_year(open_html(input('Введите название html-файла с русским текстом в кодировке utf-8:')))
