#1
perro = {}  
#2
perro['Nombre'] = 'Pulga'
perro['Color'] = 'Negro'
perro['Raza'] = 'Callejera'
perro['Patas'] = 4
perro['Edad'] = 1
#3
estudiante = {
    'Nombre': 'Camila Yaretzi',
    'Apellido': 'Landaverde Garcia',
    'Genero': 'Femenino',
    'Edad': 18,
    'Estado civil': 'Soltera',
    'Habilidades': ['Escritura', 'Comunicacion'],
    'Pais': 'Mexico',
    'Ciudad': 'Aguascalientes',  
    'Direccion': 'Republica de Uruguay'  
}
#4
longEstudi = len(estudiante)
print('La longitud del diccionario es:', longEstudi)  
#5
habilidades = estudiante['Habilidades']
print('Habilidades:', habilidades)
print('El tipo de dato de las habilidades es:', type(habilidades))
#6
estudiante['Habilidades'].append('Dibujo')
estudiante['Habilidades'].append('Programacion')  
print('Las habilidades se han actualizado:', estudiante['Habilidades']) 
#7
claveEstudi = list(estudiante.keys())
print('Las claves del estudiante son:', claveEstudi) 
#8
valorEstudi = list(estudiante.values())
print('Los valores del estudiante son:', valorEstudi)  
#9
tuplaEstudi = list(estudiante.items())
print('Diccionario como lista de tuplas:', tuplaEstudi)  
#10
del estudiante['Estado civil']
print('Se eliminó "Estado civil":', estudiante)
#11
del perro
print('El diccionario de "perro" ha sido eliminado.')
