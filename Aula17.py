# num = (2, 5, 9, 1)
# num [2]=3
# print(num)
#não pode ser inserido porque é um tupla. 
#-------------------------
#Devemos vamos declarar como lista. 
num =[2, 5, 9, 1]
num[2] = 3
print(num)
#para adicionar valor 
num =[2, 5, 9, 1]
num[2] = 3
num.append(7)
print(num)
#para colocar em ordem crescente
num =[2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
print(num)
#ordem inversa
num =[2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
print(num)
#quantos elementos tem 
num =[2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')
#adicionar valores 
num =[2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,0) #na posição 2 inseri o numero 0
print(num)
print(f'Essa lista tem {len(num)} elementos')
#remoção de elementos
num =[2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,0) #na posição 2 inseri o numero 0
num.pop(2)#remove o ultimo elemento, ou você pode passar o indice
print(num)
print(f'Essa lista tem {len(num)} elementos')
#usando o remove
num =[2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2) #na posição 2 inseri o numero 0
num.remove(2)#elimina o primeiro numero da lista
print(num)
print(f'Essa lista tem {len(num)} elementos')
#outra forma de inserir valores
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}!')
print('cheguei ao final da lista')
# python faz uma ligação entre as listas, para excluir vinculo 
a= [2, 3, 4, 7]
b= a
b= a[:]#para excluir vinculo 
b[2] = 8
print(f'Lista A:{a}')
print(f'Lista B:{b}')
