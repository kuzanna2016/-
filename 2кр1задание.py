# 2 вариант 1 задание

import re

with open('mystem.xml', encoding='utf-8') as f:
    mystem = f.read()
    
symbols = re.search(r'<body>(.+?)</body></html>', mystem, flags=re.DOTALL).group(1)
print(symbols)

with open('bodysymbols.txt','w',encoding='utf-8') as f:
    f.write('Число символов внутри тега body -')
    f.write(str(len(symbols)))
