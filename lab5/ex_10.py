import re

pattern = r'[A-Z][^A-Z]*'
text = 'CavelCase'

result = re.findall(pattern, text)
result2 = []
for i in result:
    result2.append(i[0].lower() + i[1:])
print(''.join(result2))