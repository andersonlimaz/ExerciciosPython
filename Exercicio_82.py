#Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente
# #Ao final, mostre o conteúdo das três listas geradas. 
# valores = []
# pares = []
# impar = []
# while True:
#     valores.append(int(input('Digite um valor: ')))
#     if valores 2 % == 0:
#         pares.append(valores)
#     else:
#         impar.append(valores)
#     resp = str(input('deseja sair : [S/N]'))
#     if resp in 'Ss':
#         break
# print(f'A lista completa é {valores}')
# print(f'A lista de pares é {pares}')
# print(f'A lista de impares é {impar}')
    
num = list ()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar: [S/N]'))
    if resp in 'Nn':
        break
print(num)
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('*' *30)
print(f'A lista completa {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')