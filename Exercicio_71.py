# Crie um programa que simule o funcionamento de um caixa eletronico. 
# No inicio, pergunte ao usuário qual será o valor a ser sacado (numero inteiro)
# e o programa vai informar quantas cédulas de cada valor será entregues 
# OBS: considere que o caixa possui cédulas de R$50,00, R$20,00, R$10,00 e R$1,00 
print('$-'*20)
print('CAIXA ELETRÔNICO')
print('$-'*20)

while True:
    valor = int(input('Qual valor será sacado? '))

    cedulas_50 = valor // 50 
    valor %= 50

    cedulas_20 = valor // 20 
    valor %= 20
    
    cedulas_10 = valor //10
    valor %= 10

    cedulas_1 = valor

    print('Quantidade de cédulas:')
    print(f'R$50,00: {cedulas_50}')
    print(f'R$20,00: {cedulas_20}')
    print(f'R$10,00: {cedulas_10}')
    print(f'R$1,00:  {cedulas_1}')

    sair = input('Deseja realizar outro saque ? [S/N]').upper().strip()

    if sair == 'N':
        break