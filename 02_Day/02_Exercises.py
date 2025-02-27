#'Dia dos:programcion en phyton'
Nom='Camila Yaretzi'
Ape='Landaverde Garcia'
NomCom='Camila Yaretzi Landaverde'
Pais='Mexico'
Cuidad= 'Aguascalientes'
Edad=18
Ano=2025
is_married=False
is_true=True
is_light_on=False
Altura,ColorOjos,Peso=1.68,'Cafes',58

# Tipo de datos
print(type(Nom))
print(type(Ape))
print(type(NomCom))
print(type(Pais))
print(type(Cuidad))
print(type(Edad))
print(type(Ano))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(Altura))
print(type(Peso))
print(type(ColorOjos))

# Largo del nombre
print(len(Nom))
print(len(Nom) > len(Ape))

# Operaciones 
num_uno, num_dos = 5, 4
total = num_uno + num_dos
diff = num_uno - num_dos
producto = num_uno * num_dos
division = num_uno / num_dos
remainder = num_uno % num_dos
exp = num_uno ** num_dos
floor_division = num_uno // num_dos

print(total, diff, producto, division, remainder, exp, floor_division)

#Cálculos con círculo
radio = 30
pi = 3.1416
area_del_circulo = pi * (radio ** 2)
circunferencia_del_circulo = 2 * pi * radio
print(area_del_circulo, circunferencia_del_circulo)

#Pedir radio al usuario y calcular área
radio_usuario = float(input('Ingrese el radio del círculo: '))
area_usuario = pi * (radio_usuario ** 2)
print('Área del círculo es:', area_usuario)

#Pedir datos del usuario
nom_usuario = input('Ingrese su nombre: ')
ape_usuario = input('Ingrese su apellido: ')
pais_usuario = input('Ingrese su país: ')
edad_usuario = int(input('Ingrese su edad: '))
print(f'Usuario: {nom_usuario} {ape_usuario}, País: {pais_usuario}, Edad: {edad_usuario}') #f indica que la cadena es una f-string

#Palabras claves (keywords)
import keyword
print(keyword.kwlist)