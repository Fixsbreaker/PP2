import re

pattern = r'[A-Z][a-z]+'
text = 'my_name_is_Alnur'

result = re.findall(pattern, text)
print(result)