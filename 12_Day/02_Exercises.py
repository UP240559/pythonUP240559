#1
import random
def list_of_hexa_colors(n):
    color = []
    for _ in range(n):
        colorN = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        color.append(colorN)
    return color
#2
def list_of_rgb_color(n):
    color = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color.append(f'rgb({r},{g},{b})')
    return color
#3
color_type=input('Ingresa el tipo de color que deseas crear (hexa o rgb): ').strip().lower()
n=int(input('¿Cuántos colores deseas generar? '))
def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_color(n)
    else:
        return 'Dato no valido'
print(generate_colors(color_type, n))  
