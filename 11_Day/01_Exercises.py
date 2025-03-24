import math

#1
def sumarSDosNum(a, b):
    return a + b

#2
def areaCircylo(r):
    return math.pi * r * r

#3
def sumarTodo(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    else:
        return 'Todos los argumentos deben ser números.'

#4
def CaF(celsius):
    return (celsius * 9/5) + 32

#5
def compEstaciones(mes):
    meses_a_estaciones = {
        'Diciembre': 'Invierno', 'Enero': 'Invierno', 'Febrero': 'Invierno',
        'Marzo': 'Primavera', 'Abril': 'Primavera', 'Mayo': 'Primavera',
        'Junio': 'Verano', 'Julio': 'Verano', 'Agosto': 'Verano',
        'Septiembre': 'Otoño', 'Octubre': 'Otoño', 'Noviembre': 'Otoño'
    }
    return meses_a_estaciones.get(mes, "Mes inválido")

#6
def calPendiente(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1) if x2 != x1 else "Indefinido (Línea vertical)"

#7
def ecuCuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (raiz1, raiz2)
    elif discriminante == 0:
        raiz = -b / (2*a)
        return (raiz,)
    else:
        parte_real = -b / (2*a)
        parte_imaginaria = math.sqrt(-discriminante) / (2*a)
        return (complex(parte_real, parte_imaginaria), complex(parte_real, -parte_imaginaria))

#8
def imprimirLista(lst):
    for item in lst:
        print(item)

#9
def invertirLista(lst):
    return lst[::-1]

#0
def capitalizarElementos(lst):
    return [item.capitalize() for item in lst]

#11
def agregarElemento(lst, item):
    lst.append(item)
    return lst

#12
def eliminarElemento(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

#13
def sumaNum(n):
    return sum(range(1, n+1))

#14
def sumaImpares(n):
    return sum(i for i in range(1, n+1) if i % 2 != 0)

#15
def sumaPares(n):
    return sum(i for i in range(1, n+1) if i % 2 == 0)
