def reverse(sentence):
    return " ".join(sentence.split()[::-1])

sentence = "Hello world"
print(reverse(sentence))
