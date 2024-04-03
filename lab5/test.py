#705, 777, 771
#+7

import re

pattern = r'\+7(?:05|77|71)\d{9}\b'

string = "+77779509290"

match = re.match(pattern, string)

if not match:
    print(match.group())
else:
    print("Данного номера не существует")
    


