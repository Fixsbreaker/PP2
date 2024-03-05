def isPalindrome(x: str) -> bool:
    if len(x) < 0:
        return False 
    length = len(x)
    if length == 1:
        return True
    return x[:length // 2] == x[-(length // 2):][::-1]

input_stream = input()
print(isPalindrome(input_stream))

