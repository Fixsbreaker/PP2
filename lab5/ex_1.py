import re

pattern = r'ab*'
text = 'abbbabbbabbbdsdsdsdsdsaaabbbadbababa'

result = re.findall(pattern, text)
print(result)
# ['abbb', 'abbb', 'abbb', 'a', 'a', 'abbb', 'a', 'ab', 'ab', 'a']