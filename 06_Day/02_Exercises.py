#1
family_members = ('Andrea', 'Jesus', 'Jose', 'Teresa')
losDos, papas = family_members[:-2], family_members[-2:]
print("Hermanos:", losDos)
print("Padres:", papas)
#2
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'eggs', 'cheese')
#3
food_stuff_tp = fruits + vegetables + animal_products
print("Tupla de alimentos:", food_stuff_tp)
#4 
food_stuff_lt = list(food_stuff_tp)
print("Lista de alimentos:", food_stuff_lt)
#5
middle_item = food_stuff_tp[len(food_stuff_tp) // 2] if len(food_stuff_tp) % 2 != 0 else food_stuff_tp[len(food_stuff_tp) // 2 - 1:len(food_stuff_tp) // 2 + 1]
print("Elemento(s) del medio:", middle_item)
#6
first_three_last_three = food_stuff_lt[:3] + food_stuff_lt[-3:]
print("Primeros tres y últimos tres elementos:", first_three_last_three)
#7
del food_stuff_tp
#8
countries = ('Sweden', 'Denmark', 'Norway', 'Finland', 'Iceland')
print("¿Estonia es un país nórdico?", 'Estonia' in countries)
print("¿Islandia es un país nórdico?", 'Iceland' in countries)
