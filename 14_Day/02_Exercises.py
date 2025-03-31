from countries import countries
from functools import reduce
from collections import defaultdict

#1
paises_mayusculas = list(map(lambda pais: pais.upper(), countries))
print("Países en mayúsculas:", paises_mayusculas)

#2
numeros = [1, 2, 3, 4, 5]
numeros_cuadrados = list(map(lambda x: x ** 2, numeros))
print("Números al cuadrado:", numeros_cuadrados)

#3
nombres = ['Camila', 'Evelyn', 'Santiago']
nombres_mayusculas = list(map(lambda nombre: nombre.upper(), nombres))
print("Nombres en mayúsculas:", nombres_mayusculas)

#4
paises_con_tierra = list(filter(lambda pais: 'tierra' in pais.lower(), countries))
print("Países que contienen 'tierra':", paises_con_tierra)

#5
paises_con_seis_caracteres = list(filter(lambda pais: len(pais) == 6, countries))
print("Países con exactamente 6 caracteres:", paises_con_seis_caracteres)

#6
paises_con_seis_o_mas = list(filter(lambda pais: len(pais) >= 6, countries))
print("Países con 6 o más letras:", paises_con_seis_o_mas)

#7
paises_que_empiezan_con_e = list(filter(lambda pais: pais.startswith('E'), countries))
print("Países que comienzan con 'E':", paises_que_empiezan_con_e)

#8 Encadenar `map` y `filter`
paises_filtrados_y_mayusculas = list(
    map(lambda pais: pais.upper(), 
        filter(lambda pais: len(pais) > 6, countries))
)
print("Países con más de 6 caracteres en mayúsculas:", paises_filtrados_y_mayusculas)

#9
def obtener_lista_de_cadenas(lista_entrada):
    return list(filter(lambda item: isinstance(item, str), lista_entrada))

lista_mista = ['Hola', 123, 'Mundo', 456, 'Python']
lista_cadenas = obtener_lista_de_cadenas(lista_mista)
print("Elementos de tipo cadena de la lista mixta:", lista_cadenas)

#10
suma_numeros = reduce(lambda x, y: x + y, numeros)
print("Suma de los números:", suma_numeros)

#11
paises_nordicos = ['Estonia', 'Finlandia', 'Suecia', 'Dinamarca', 'Noruega', 'Islandia']
oracion = reduce(lambda acc, pais: acc + ', ' + pais, paises_nordicos)
oracion = oracion + ' son países del norte de Europa.'
print("Oración con países:", oracion)

#12
def categorizar_paises(patron):
    return [pais for pais in countries if patron.lower() in pais.lower()]

patron = 'land'
resultado = categorizar_paises(patron)
print("Países que coinciden con el patrón 'land':", resultado)

#13
def contar_paises_por_primera_letra():
    contador_letras = defaultdict(int)
    for pais in countries:
        primera_letra = pais[0].upper()
        contador_letras[primera_letra] += 1
    return dict(contador_letras)

conteo_letras = contar_paises_por_primera_letra()
print("Conteo de países por primera letra:", conteo_letras)

#14
def obtener_primeros_diez_paises():
    return countries[:10]
primeros_diez_paises = obtener_primeros_diez_paises()
print("Primeros diez países:", primeros_diez_paises)

#15
def obtener_ultimos_diez_paises():
    return countries[-10:]
ultimos_diez_paises = obtener_ultimos_diez_paises()
print("Últimos diez países:", ultimos_diez_paises)
