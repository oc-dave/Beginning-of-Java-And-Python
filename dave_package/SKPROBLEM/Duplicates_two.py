nums = [4, 3, 2, 2, 3, 3]
digits = [i for i in nums if nums.count(i) > 0]

print(digits)

# def is_subsequence(s, t):
#     if len(s) < len(t):
#         return False
#
#     for i in range(len(t)):
#         if s[i:] == t[i:]:
#             return True
#
#     return False
#
#
# s = "ace"
# t = "abcde"
#
# print(is_subsequence(s, t))