num = int(input("Enter a number: "))
for x in range(1, 13):
    print('\t')
    for y in range(1, num+1):
        print(f"{x} x {y} = {x * y}", end="\t\t")
