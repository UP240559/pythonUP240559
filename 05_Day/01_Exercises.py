listaVacia=[]  # 1
lista=[132, 242, 343, 434, 556, 656, 659]  # 2
print(len(lista))  # 3

# 4
print(lista[0])
print(lista[len(lista)//2])
print(lista[-1])

mixed_data_types=['Camila', 18, 168, 'Soltera', 'Republica Uruguay 1805']  # 5

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']  # 6
print(it_companies)  # 7
print(len(it_companies))  # 8

# 9
print(it_companies[0])  
print(it_companies[len(it_companies)//2])  
print(it_companies[-1])  

# 10
it_companies[3] = 'Samsung'  
print(it_companies)  

# 11
it_companies.append('Fedex')  
print(it_companies)  

# 12
it_companies.insert(len(it_companies)//2, 'Netflix')  
print(it_companies)  

# 13
it_companies[0] = it_companies[0].upper()  
print(it_companies)  

print('#;  '.join(it_companies))  # 14
print('Google' in it_companies)  # 15
it_companies.sort()  # 16
print(it_companies)  

# 17
it_companies.reverse()  
print(it_companies)  
print(it_companies[:3])  # 18 
print(it_companies[-3:])  # 19
print(it_companies[len(it_companies)//2-1:len(it_companies)//2+1])  # 20 

# 21
it_companies.pop(0)  
print(it_companies)  

# 22
it_companies.pop(len(it_companies)//2)  
print(it_companies)  

# 23
it_companies.pop()  
print(it_companies)  

# 24
it_companies.clear()  
print(it_companies)  

del it_companies  # 25 

# 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']  
back_end = ['Node', 'Express', 'MongoDB']  
full_stack = front_end + back_end  
print(full_stack)  

# 27
full_stack.insert(full_stack.index('Redux') + 1, 'Python')  
full_stack.insert(full_stack.index('Python') + 1, 'SQL')  
print(full_stack)
