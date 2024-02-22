import re

pattern = r'[A-Z][^A-Z]*'
stroka = 'QwEwQeqWe'
print(re.findall(pattern, stroka))