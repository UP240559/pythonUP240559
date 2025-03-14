#1
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print(f'Lista: {len(age)}')
print(f'Conjunto: {len(age_set)}')

if len(age_set) > len(age):
    print('\nEl conjunto es más largo que la lista')
elif len(age_set) == len(age):
    print('\nEl conjunto es igual que la lista')
else:
    print('\nEl conjunto es más corto que la lista')

#2
# String: Una secuencia de caracteres, inmutable
cadena = 'Hola Mundo'
print('String:', cadena)
print('Elemento 0:', cadena[0])  
# List: Una colección ordenada, mutable y permite duplicados
#Se puede modificar
lista = ['manzana', 'banana', 'cereza', 'manzana']
print('\nList:', lista)
lista.append('naranja')  
print('Nueva lista:', lista)
#Tuple: Una colección ordenada, inmutable y permite duplicados
tupla = ('rojo', 'verde', 'azul', 'rojo')
print('\nTuple:', tupla)
print('Elemento 1):', tupla[1])  
#Set: Una colección desordenada, mutable y no permite duplicados
#El set elimina duplicados automáticamente
conjunto = {'perro', 'gato', 'conejo', 'perro'}
print('\nSet:', conjunto)  
conjunto.add('hamster')  
print('Nuevo set:', conjunto)

#3
maestro = 'Soy un maestro y me encanta inspirar y enseñar a las personas'
p = maestro.split()  
pUnicas = set(p)  
print(f'\nLas palabras que no se repiten son: {pUnicas}')
print(f'Cantidad de palabras únicas: {len(pUnicas)}')
