list1 = [20,30, 30, 60, 65, 75, 80]
list2 = [42, 30, 80, 65, 68, 88, 95]

intersection = []
for element in list1:
    if element in list2:
        intersection.append(element)

intersect = tuple(intersection)
print(intersect)
