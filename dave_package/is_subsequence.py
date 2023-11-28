def is_subsequence(s, t):
    s_index = 0
    for char in t:
        if s_index == len(s):
            break
        if char == s[s_index]:
            s_index += 1
    return s_index == len(s)


s = "ace"
t = "abcde"

print(is_subsequence(s, t))
