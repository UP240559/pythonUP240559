#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print('Números negativos o cero:', negative_and_zero)
#2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist in list_of_lists for subsublist in sublist for item in subsublist]
print('Lista aplanada:', flattened_list)
#3
result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print('Lista de tuplas con exponentes:', result)
#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for sublist in countries for country in sublist]
print('Lista de países y ciudades transformada:', flattened_countries)
#5
dict_countries = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for sublist in countries for country in sublist]
print('Lista de diccionarios de países y ciudades:', dict_countries)
#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{name[0][0]} {name[0][1]}" for name in names]
print('Lista de nombres concatenados:', concatenated_names)
#7
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
m = slope(1, 2, 3, 6)
print('Pendiente de la recta:', m)
intercept = lambda x1, y1, m: y1 - m * x1
b = intercept(1, 2, m)
print('Intersección de la recta:', b)
