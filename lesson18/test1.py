import re

text = 'Московское время 10:36:06'
res = re.search(r'([0-9]{2}[:]{0,1}){3}', text)
print(res.group())
