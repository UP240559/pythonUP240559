#1
import random
import string

def random_user_id ():
    return''.join(random.choices(string.ascii_letters + string.digits, k=6))
print(random_user_id())
#2
def user_id_gen_by_user():
    tamano=int(input('Ingresa la cantidad de caracteres para el ID:'))
    numId=int(input('Ingresa la cantidad de ID a generara: '))
    ids = []
    for _ in range(numId):
        #Aqui se generarn los ids
        ids.append(''.join(random.choices(string.ascii_letters + string.digits, k=tamano)))
    return "\n".join(ids)
print(user_id_gen_by_user())
#3
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r},{g},{b})'
print('\nGenerador de colores RGB aleatorios:\n', rgb_color_gen())

