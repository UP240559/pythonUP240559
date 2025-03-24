import statistics

#1
def paresImpares(n):
    pares = sum(1 for i in range(1, n+1) if i % 2 == 0)
    impares = n - pares
    return f'El número de pares es {pares}. El número de impares es {impares}.'

#2
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

#3
def estaVacio(valor):
    if isinstance(valor, (list, tuple, set)):
        return len(valor) == 0
    elif isinstance(valor, dict):
        return len(valor.keys()) == 0
    elif valor == "":
        return True
    return False

#4
def calMedia(lst):
    return statistics.mean(lst)

def calMediana(lst):
    return statistics.median(lst)

def calModa(lst):
    try:
        return statistics.mode(lst)
    except statistics.StatisticsError:
        return 'No hay una moda única'

def calRango(lst):
    return max(lst) - min(lst)

def calVarianza(lst):
    return statistics.variance(lst)

def calDesviacion_estandar(lst):
    return statistics.stdev(lst)
