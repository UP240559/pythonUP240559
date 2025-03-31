#1
#Con map 
numeros = [1, 2, 3, 4]
def cuadrado(x):
    return x ** 2
cuadrados = map(cuadrado, numeros)
print("Resultado de map (cuadrados):", list(cuadrados)) 

#Con filter 
def es_par(x):
    return x % 2 == 0

pares = filter(es_par, numeros)
print("Resultado de filter (pares):", list(pares))  

#Con reduce 
from functools import reduce
def sumar(x, y):
    return x + y

suma_total = reduce(sumar, numeros)
print("Resultado de reduce (suma):", suma_total)  

#2
def aplicar_funcion(func, valor):
    return func(valor)

resultado = aplicar_funcion(lambda x: x * 2, 5)
print("Resultado de función de orden superior:", resultado)  

def funcion_exterior(variable_exterior):
    def funcion_interior(variable_interior):
        return variable_exterior + variable_interior
    return funcion_interior

cierre = funcion_exterior(10)
print("Resultado de cierre:", cierre(5))  

#Decorador
def decorador(func):
    def envoltorio():
        print("Antes de la llamada")
        func()
        print("Después de la llamada")
    return envoltorio

@decorador
def saludar():
    print("¡Hola!")

saludar()

#3
paises = ['Mexico', 'Canada', 'Colombia', 'Francia']
print("Lista de países:")
for pais in paises:
    print(pais)

nombres = ['Camila', 'Ely', 'Alondra', 'Evelyn']
print("\nLista de nombres:")
for nombre in nombres:
    print(nombre)

numeros = [33, 17, 54, 45]
print("\nLista de números:")
for numero in numeros:
    print(numero)
