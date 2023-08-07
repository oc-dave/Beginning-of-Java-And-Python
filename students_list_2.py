import json

names = ['Joe','Daniel','Seyi','Kelvin','Muhammed','Hakimi','Segun','Ashley','Seyi']

count_Segun = 0
count_Seyi = 0

for name in names:
    if name == 'Segun':
        count_Segun += 1
    elif name == 'Seyi':
        count_Seyi += 1

new_list = [['Segun',count_Segun],['Seyi',count_Seyi]]
new_dict = json.loads(json.dumps(dict(new_list)))
print(new_dict)

# from collections import Counter
#
# names = ['Joe', 'Daniel', 'Seyi', 'Kelvin', 'Muhammed', 'Hakimi', 'Segun', 'Ashley', 'Seyi']
#
# counts = Counter(names)
# new_dict = dict(counts.items())  # Converts Counter object to a dictionary
# print(new_dict)
