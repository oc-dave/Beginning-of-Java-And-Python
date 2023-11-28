from collections import Counter


def isAnagram(a, b):
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return sorted(a) == sorted(b)


a = "anagram"
b = "nagaram"
result = isAnagram(a, b)
print(result)


def isAnagram(s, t):
    return Counter(s) == Counter(t)


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))
