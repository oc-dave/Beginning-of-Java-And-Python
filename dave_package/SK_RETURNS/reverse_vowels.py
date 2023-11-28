
def reverse_vowels(input):
    input = input.lower()
    vowels = "aeiouAEIOU"
    output = ""
    vowel_list = [i for i in input if i in vowels]

    for i in input:
        if i in vowels:
            output += vowel_list.pop()
        else:
            output += i
    return output


input = "leetcode"
print(reverse_vowels(input))
