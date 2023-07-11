#Crie um programa onde usuario possa digitar 7 valores númericos e cadastre-os em uma lista única
# #que mantenha separados os valores pares e imparaes. No final, mostre os valores pares e impares em ordem crescente
# lista = []
# pares = []
# impares = []

# for _ in range(7):
#     numero = int(input('Digite um valor numérico: '))
#     lista.append(numero)

#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)

# pares.sort()
# impares.sort()

# print(f'Lista completa: {lista}')
# print(f'Números pares: {pares}')
# print(f'Números ímpares: {impares}')

num = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c} valor: '))
    if valor % 2 ==0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-*' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram:{num[0]}')
print(f'Os valores impares digitados foram:{num[1]}')