#1
sumTotal=0
for i in range(101):
    sumTotal += i
print("La suma de todos los números es:", sumTotal)
#2
sumPar=0
sumImpar=0
for i in range(101):
    if i % 2 == 0:
        sumPar += i
    else:
        sumImpar += i
print(f"La suma de todos los números pares es: {sumPar}")
print(f"La suma de todos los números impares es: {sumImpar}")
