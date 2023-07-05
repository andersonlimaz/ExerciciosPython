#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastra-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. 
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
# num = []
# while True:
#     num.append(int(input('Digite um valor númerico? ')))
#     print('Valor adicionado com sucesso! ') 
#     cont = str(input('Quer continuar? [S/N]')).upper().split()[0]
#     if cont == "N":
#         break
     
# num.sort()
# print(f'Os valores digitos foram: {num}')
#correção 
numeros = list()
while True:
    n = int(input('Digite um valor?'))
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado!')
    else:
        print('Valor duplicado! não vou adicionar!')

    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r in 'Nn':
        break
print('+'*60)
numeros.sort()
print(f'Você digitou os valores {numeros}')
