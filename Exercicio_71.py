# Crie um programa que simule o funcionamento de um caixa eletronico. 
# No inicio, pergunte ao usuário qual será o valor a ser sacado (numero inteiro)
# e o programa vai informar quantas cédulas de cada valor será entregues 
# OBS: considere que o caixa possui cédulas de R$50,00, R$20,00, R$10,00 e R$1,00 
# print('$-'*20)
# print('CAIXA ELETRÔNICO')
# print('$-'*20)

# while True:
#     valor = int(input('Qual valor será sacado? '))

#     cedulas_50 = valor // 50 
#     valor %= 50

#     cedulas_20 = valor // 20 
#     valor %= 20
    
#     cedulas_10 = valor //10
#     valor %= 10

#     cedulas_1 = valor

#     print('Quantidade de cédulas:')
#     print(f'R$50,00: {cedulas_50}')
#     print(f'R$20,00: {cedulas_20}')
#     print(f'R$10,00: {cedulas_10}')
#     print(f'R$1,00:  {cedulas_1}')

#     sair = input('Deseja realizar outro saque ? [S/N]').upper().strip()

#     if sair == 'N':
#         break

#correção

print('=' * 30)
print('{:^30}'.format('Banco Andersão'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0 
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd} ')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre !')
