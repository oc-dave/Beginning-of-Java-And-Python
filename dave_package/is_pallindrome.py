def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False


name = input("Enter a palindrome: ")
print(is_palindrome(name))
