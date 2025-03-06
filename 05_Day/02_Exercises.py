edades = [18, 21, 19, 20, 23, 25, 27, 17, 24, 26]#1
#2
edades.sort()
edadMin = min(edades)
edadMax = max(edades)
print(f"Edad mínima: {edadMin}")
print(f"Edad máxima: {edadMax}")

edades.append(edadMin)
edades.append(edadMax)
print(f"Lista de edades después de agregar min y max: {edades}")

if len(edades) % 2 == 0:
    mediana = (edades[len(edades)//2 - 1] + edades[len(edades)//2]) / 2
else:
    mediana = edades[len(edades)//2]
print(f"Edad mediana: {mediana}")

promedio = sum(edades) / len(edades)
print(f"Edad promedio: {promedio}")

rango = edadMax - edadMin
print(f"Rango de edades: {rango}")

comparacion_min = abs(edadMin - promedio)
comparacion_max = abs(edadMax - promedio)
print(f"Comparación min - promedio: {comparacion_min}")
print(f"Comparación max - promedio: {comparacion_max}")

paises = ['China', 'Rusia', 'EE.UU.', 'Finlandia', 'Suecia', 'Noruega', 'Dinamarca']#2
#3
if len(paises) % 2 == 0:
    paises_medios = paises[len(paises)//2 - 1: len(paises)//2 + 1]
else:
    paises_medios = paises[len(paises)//2]
print(f"País(es) del medio: {paises_medios}")

if len(paises) % 2 == 0:
    mitad1 = paises[:len(paises)//2]
    mitad2 = paises[len(paises)//2:]
else:
    mitad1 = paises[:len(paises)//2 + 1]
    mitad2 = paises[len(paises)//2 + 1:]
print(f"Primera mitad de países: {mitad1}")
print(f"Segunda mitad de países: {mitad2}")
#4
primeros_tres, *paises_nordicos = paises
print(f"Primeros tres países: {primeros_tres}")
print(f"Paises nórdicos: {paises_nordicos}")
