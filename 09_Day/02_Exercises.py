#1
calf = float(input('Ingresa tu calificación: '))

if 80 <= calf <= 100:
    print('Sacaste una A')
elif 70 <= calf < 80:
    print('Sacaste una B')
elif 60 <= calf < 70:
    print('Sacaste una C')
elif 50 <= calf < 60:
    print('Sacaste una D')
else:
    print('Sacaste una F')

#2
mes = input('Ingrese el mes actual: ').strip().lower() #Para que no se te olvide
#.strip() elimina los espacios antes y despues, y .lower() convierte el texto a minusculas
if mes in ['septiembre', 'octubre', 'noviembre']:
    print('La estación es Otoño.')
elif mes in ['diciembre', 'enero', 'febrero']:
    print('La estación es Invierno.')
elif mes in ['marzo', 'abril', 'mayo']:
    print('La estación es Primavera.')
elif mes in ['junio', 'julio', 'agosto']:
    print('La estación es Verano.')
else:
    print('Mes no existente')

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
comprobarFrut = input('Ingresa una fruta: ').strip().lower()
if comprobarFrut in fruits:
    print('Esa fruta ya existe en la lista')
else:
    fruits.append(comprobarFrut)
    print('Nueva lista de frutas:', fruits)