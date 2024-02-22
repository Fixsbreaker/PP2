import re

pattern = r'ab{2,3}'
text = 'abbbabbabbbbbb'

result = re.findall(pattern, text)
print(result)

# ['abbb', 'abb', 'abbb']
