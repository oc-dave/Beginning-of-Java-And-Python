list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
answer = [i ** 2 for i in list1]
answer2 = [i for i in list1 if i % 2 == 0]
answer3 = [i for i in list1 if i % 2 == 1]

print(answer)
print(answer2)
print(answer3)
