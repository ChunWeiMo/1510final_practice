mealtimes = ['breakfast', 'second breakfast', 'lunch', 'tea', 'dinner']
meals = ['eggs', 'yoghurt', 'soup', 'jam and bread', 'fish', 'chocolate']

zip_1 = zip(mealtimes, meals)
print(zip(mealtimes, meals))
print(zip_1)

list_1 = list(zip_1)
print(list_1)

for set_1 in zip_1:
    print(set_1)
