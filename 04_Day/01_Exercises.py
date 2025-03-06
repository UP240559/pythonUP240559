string1=''.join(['Thirty','','Days','','Of','','Python'])#1
print(string1)
string1=''.join(['Coding','','For','','All'])#2
print(string1)
company='Coding For All'#3
print(company)#4
print(len(company))#5
M=company.upper()#mayusculas 6
print(M)
m=company.lower()#minusculas 7
print(m)
print(company.capitalize())#8
print(company.title())#8
print(company.swapcase())#8
cortarPalabra = company.split()[0]#9
print(cortarPalabra) 

if 'Coding' in company: #10
    print('La cadena tiene la palabra "Coding"')

nuevaString=company.replace('Coding','Python')#11
print(nuevaString) 
frase = "Python for Everyone"
nueva_frase = frase.replace("Everyone", "All")#12
print(nueva_frase)
divString=company.split()#13
print(divString)

#14
Aplicaciones = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
listaComas = Aplicaciones.split(', ')
print(listaComas) 

print(company[0])#15
print(company[-1])#16
print(company[10])#17

acronimo= ''.join([word[0] for word in 'Python For Everyone'.split()])#18
print(acronimo)  
acronimo2 = ''.join([word[0] for word in 'Coding For All'.split()])#19
print(acronimo2) 
print(company.index('C'))#20
print(company.index('F'))#21
print(company.rfind('l'))#22

frase = 'You cannot end a sentence with because because because is a conjunction'
print(frase.find('because'))#23
print(frase.rindex('because'))#24
print(frase[31:62])#25

print(company.startswith('Coding'))#26
print(company.endswith('coding'))#27
cadenaEspacios = '   Coding For All      '#28
print(cadenaEspacios.strip()) 

print('30DaysOfPython'.isidentifier())#29
print('thirty_days_of_python'.isidentifier())#30

bibliotecas = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']#31
print('# '.join(bibliotecas)) 

print("I am enjoying this challenge.\nI just wonder what is next.")#32

print("Name\tAge\tCountry\tCity")#33
print("Camila\t18\tMexico\tAguascalientes")#34


#35
radio = 10  
area = 3.14 * radio ** 2
print(f"El área de un círculo con radio 10 es {area} metros cuadrados.")  

#36
print(f"8 + 6 = {8 + 6}")  
print(f"8 - 6 = {8 - 6}")  
print(f"8 * 6 = {8 * 6}") 
print(f"8 / 6 = {8 / 6:.2f}")  
print(f"8 % 6 = {8 % 6}")  
print(f"8 // 6 = {8 // 6}")  
print(f"8 ** 6 = {8 ** 6}")  






