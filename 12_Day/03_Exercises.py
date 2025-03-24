#1
import random
#Esta en mymodule.py)
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
#2
def unique_random_numbers():
    return random.sample(range(10), 7)
my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)
print("Lista mezclada:", shuffled_list)
random_numbers = unique_random_numbers()
print("Números aleatorios únicos:", random_numbers)
