# # # numbers = [10, 20, 30, 40, 50]
# # # total = 0
# # #
# # # for x in numbers:
# # #     total += x
# #
# # print(total)
#
# numbers = [10, 20, 30, 40, 50]
# total = 0
#
# for x in numbers[0::2]:
#     total += x
#
# print(total)
#
# # numbers = [10, 20, 30, 40, 50]
# # total = 0
# #
# # for x in numbers[1::2]:
# #     total += x
# #
# # print(total)

numbers = [10, 20, 30, 40, 50]
square = []
total = 0

for x in numbers:
    square = x ** 2
    square.append(square)
    total += square

print("Squared numbers:", square)
print("Sum of squared numbers:", total)
