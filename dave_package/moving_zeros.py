# list1 = [4, 3, 0, 2, 0, 4, 10, 12]
# new_list = []
# for i in list1:
#     if i != 0:
#         new_list.append(i)
# for i in list1:
#     if i == 0:
#         new_list.append(i)
# print(new_list)

list1 = [4, 3, 0, 2, 0, 4, 10, 12]

for i in range(len(list1)):
    if list1[i] == 0:
        list1.pop(i)
        list1.append(0)
print(list1)

