import re

pattern = r'a.+b'
text = 'asdsdb'

result = re.findall(pattern, text)
print(result)