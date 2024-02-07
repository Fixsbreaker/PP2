def is_palindrome(sentence):
    sentence = sentence.replace(" ", "").lower()
    return sentence == sentence[::-1]

print(is_palindrome("a man a plan a canal panama"))  # вывод: True
print(is_palindrome("racecar"))                     # вывод: True
print(is_palindrome("hello"))                       # вывод: False
