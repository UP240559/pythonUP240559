edad= 18
altura= 5.75 
numComple= 3 + 4j  

#Area de un triángulo
base= float(input('Ingresa la base: '))
altura= float(input('Ingresa la altura: '))
area= 0.5 * base * altura
print(f'El área del triángulo es {area}')

#Perimetro de un triangulo
a= float(input('Ingresa el lado a del triangulo: '))
b= float(input('Ingresa el lado b del triangulo: '))
c= float(input('Ingresa el lado c del triangulo: '))
peri = a + b + c
print(f'El perimetro del triangulo es: {peri}')

#Area y perimetro de un rectangulo
long= float(input('Ingresa la longitud del rectangulo: '))
ancho= float(input('Ingresa el ancho del rectángulo: '))
area= long  * ancho
peri= 2 * (long + ancho)
print(f'Area del rectangulo: {area}')
print(f'Perimetro del rectángulo: {peri}')

#Area y circunferencia de un circulo
radio = float(input('Ingresa el radio del círculo: '))
pi = 3.14
area = pi * radio * radio
cirf = 2 * pi * radio
print(f'Area del circulo: {area}')
print(f'Circunferencia del circulo: {cirf}')

#Calcula la pendiente, la intersección x y la intersección y 
pendiente = 2 #y = 2x - 2, la pendiente es 2
interseccion_x = 2  #y=0, 0 = 2x - 2 , 2x = 1
interseccion_y = -2  # Cuando x = 0, y = -2
print(f"Pendiente: {pendiente}, Intersección con el eje X: {interseccion_x}, Intersección con el eje Y: {interseccion_y}")

#Calcular la pendiente y la distancia euclidiana entre los puntos (2,2) y (6,10)
import math
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f'Pendiente: {pendiente}')
print(f'Distancia euclidiana: {distancia}')

#Comparar las pendientes de las tareas 8 y 9
pendiente_8 = 2
pendiente_9 = (y2 - y1) / (x2 - x1)

if pendiente_8 == pendiente_9:
    print('Las pendientes son iguales')
else:
    print('Las pendientes son diferentes')

#Calcular y = x^2 + 6x + 9 para varios valores de x
for x in range(-10, 10):
    y = x**2 + 6*x + 9
    print(f'Para x = {x}, y = {y}')
    if y == 0:
        print(f'x = {x} da y = 0')

# 12. Encontrar la longitud de python y dragon
long_python = len('python')
long_dragon = len('dragon')
print(long_python == long_dragon)  # La comparación falsa

#Usar and
if 'on' in 'python' and 'on' in 'dragon':
    print('La subcadena on está presente en ambos')
else:
    print('La subcadena no se encuentra en ambos')

#Comprobar si jargon está en una oración usando el operador in
oracion = 'Espero que este curso no esté lleno de jerga'
if 'jerga' in oracion:
    print('La palabra está en la oración ')
else:
    print('La palabra jerga no está en la oración')

#Encontrar la longitud del texto
long_python = len('python')
float_long = float(long_python)
str_long = str(float_long)
print(f'Longitud de python como flotante: {float_long}')
print(f'Longitud de python como cadena: {str_long}')

#Comprobar si un número es par en Python
numero = int(input('Introduce un numero: '))
if numero % 2 == 0:
    print(f'{numero} es par.')
else:
    print(f'{numero} es impar')

#Comprobar si la división entera de 7 por 3 es igual al valor entero de 2.7
if 7 // 3 == int(2.7):
    print('La división entera de 7 por 3 es igual al valor entero de 2.7.')
else:
    print('La división entera de 7 por 3 no es igual al valor entero de 2.7.')

#Comprobar si el tipo de '10' es igual al tipo de 10
if type('10') == type(10):
    print('Los tipos son iguales')
else:
    print('Los tipos son diferentes')

#Comprobar si int('9.8') es igual a 10
try:
    if int('9.8') == 10:
        print('El valor entero de 9.8 es igual a 10.')
except ValueError:
    print('No se puede convertir 9.8 a un entero.')

#Calcular las ganancias semanales basadas en las horas y la tarifa
horas = float(input('Ingresa las horas: '))
tarifa = float(input('Ingresa la tarifa por hora: '))
pago = horas * tarifa
print(f'Tu ganancia semanal es {pago}')

#Calcular la cantidad de segundos que una persona ha vivido según los años
años = int(input('Ingresa el número de años que has vivido: '))
segundos = años * 365 * 24 * 60 * 60 
print(f'Has vivido {segundos} segundos')

#Crear una tabla
import random

# Imprimir la tabla con los valores aleatorios
import random
for i in range(1, 6):  
    num = random.randint(1, 10) 
    print(f"{num} {num**2} {num**3} {num**4} {num**5}")



