import re

pattern = r'[A-Z][^A-Z]*'
text = 'QweQrtyYrwww'
result = re.findall(pattern, text)
print(' '.join(result))