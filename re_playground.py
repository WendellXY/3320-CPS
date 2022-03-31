import re

text = 'hello world <a>emm</a>啊啊啊啊啊啊<a>这是链接</a>'

print(re.compile("[^\x00-\xff]+", re.I).findall(text))