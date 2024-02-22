import re

pattern = r'_'
text = 'my_name_is_Alnur'

result = re.split(pattern, text)
result2 = []
for i in result:
    result2.append(i[0].upper() + i[1:])
print(''.join(result2))