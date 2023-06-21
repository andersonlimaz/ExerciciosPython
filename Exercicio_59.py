#CRIE UM PROGRAMA QUE LEIA DOIS VALOR E VAI MOSTRAR UM MENU NA TELA 
#[1] SOMAR
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NÚMEROS
#[5] SAIR DO PROGRAMA
# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO. 
sair = False
while not sair:
    valor1 = (int(input('Digite o primeiro valor:')))
    valor2 = (int(input('Digite o segundo valor:')))
    
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''') 
    opção = int(input('Qual opação: '))
    if opção == 1:
        print('Você escolheu a opção SOMA !')
        soma = valor1 + valor2
        print('Resultado: {}'.format(soma))
    elif opção == 2: 
         print('Voce escolheu opção Multiplicação')
         mult = valor1 * valor2
         print('Resultado: {}'.format(mult))
    elif opção == 3:
        if valor1 > valor2:
            print('Valor maior {}'.format(valor1))
        else:
             valor2 > valor1
             print('Valor maior {}'.format(valor2))
    elif opção == 4:
            valor1 = (int(input('Digite o primeiro valor:')))
            valor2 = (int(input('Digite o segundo valor:')))
    else:
         opção == 5 
print('você saiu do jogo !')         