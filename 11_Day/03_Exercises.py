import math

#1
def esPrimo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#2
def todosUnicos(lst):
    return len(lst) == len(set(lst))

#3
def mismoTipo(lst):
    if len(lst) == 0:
        return True
    primer_tipo = type(lst[0])
    return all(type(item) == primer_tipo for item in lst)

#4
def pythonVariable(nombre):
    return nombre.isidentifier()

#5
def masHablados():
    idiomas = [
        ('Chino Mandarín', 918000000),
        ('Español', 460000000),
        ('Inglés', 377000000),
        ('Hindi', 310000000),
        ('Árabe', 274000000),
        ('Bengalí', 273000000),
        ('Portugués', 264000000),
        ('Ruso', 255000000),
        ('Japonés', 125000000),
        ('Lahnda (Punyabí)', 118000000)
    ]
    idiomas.sort(key=lambda x: x[1], reverse=True)
    return idiomas[:10] 

#6
def masPoblados():
    paises = [
        ('China', 1402112000),
        ('India', 1366417754),
        ('EE.UU.', 329484123),
        ('Indonesia', 270625568),
        ('Pakistán', 220892331),
        ('Brasil', 212559417),
        ('Nigeria', 206139589),
        ('Bangladesh', 163046161),
        ('Rusia', 145912025),
        ('México', 128933395)
    ]
    paises.sort(key=lambda x: x[1], reverse=True)
    return paises[:10]
