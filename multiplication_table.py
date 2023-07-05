num = int(input("Enter a number: "))
for x in range(1, 101):
    print('')
    for y in range(1, num + 1):
        print(f"{y} x {x} = {x * y:<20}", end="\t")


print(" ")
