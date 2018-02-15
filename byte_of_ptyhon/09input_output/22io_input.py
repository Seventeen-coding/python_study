#encoding=UTF-8

#倒退 背面
def reverse(text):
    return text[::-1]

#回文
def is_palindrome(text):
    return text == reverse(text)

something = input("Enter text: ")

if is_palindrome(something):
    print("yes, it is a palindrome")
else:
    print("no, it is not a palindrome")


