sample_list = ['Male','Female','female','male','male','male','Female','male','Female','Male','Female','Male','female']

count_female = 0
count_male = 0
for sample in sample_list:
    if sample.casefold() == 'Female'.casefold():
        count_female = count_female + 1
    elif sample.casefold() == 'Male'.casefold():
        count_male = count_male + 1

new_list = [['Male',count_male],['female',count_female]]
print(new_list)