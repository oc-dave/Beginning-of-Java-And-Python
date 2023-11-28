import re


def remove_hash(s, t):
    s = re.sub(r'.#', '', s)
    t = re.sub(r'.#', '', t)

    return len(s) == len(t)


input_string1 = "a##d"
input_string2 = "ac#d"

result = remove_hash(input_string1, input_string2)
print(result)  # Output: True

#     s = "ab#d"
#     t = "ac#d"
#
#     return s.replace("b#", "") == t.replace("c#", "")
#
#
# print(hash_is_backspace("ab#d", "ac#d"))
#
#
# def hash_is_backspace_two(s, t):
#     s = "aq##"
#     t = "c#d#"
#
#     return s.replace("aq##", "") == t.replace("c#d#", "")
#
#
# print(hash_is_backspace_two("aq##", "c#d#"))
#
#
# def hash_is_backspace_three(s, t):
#     s = "aq#"
#     t = "r"
#
#     return s.replace("aq#", "") == "r"
#
#
# print(hash_is_backspace_three("aq#", "r"))
