
def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word


name = input("Enter a palindrome: ")
print(is_palindrome(name))
