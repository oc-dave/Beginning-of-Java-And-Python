def reverse(word):
    words = word.split()
    words = [i[::-1] for i in words]
    return " ".join(words)


reversed_word = "a better place"
print(reverse(reversed_word))

