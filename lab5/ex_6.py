import re

pattern = r'[,. ]'
repl = r':'
text = input()
# with open("row.txt", encoding="UTF-8") as file_in:
#     lines = file_in.readlines()
# for line in lines:
print(re.sub(pattern, repl, text))
