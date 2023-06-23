#CRIE UM PROGRAMA QUE LEIA DOIS VALOR E VAI MOSTRAR UM MENU NA TELA 
#[1] SOMAR
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NÚMEROS
#[5] SAIR DO PROGRAMA
# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO. 
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:# enquanto for diferente de 5 roda o loop. 
    print(''' 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')
    opção = int(input('Qual sua é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação entre {} X {} = {}'.format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} maior valor é {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('Entre {} e {} maior valor é {}'.format(n1, n2, maior))
        elif n1 == n2:
            print('Os valores {} e {} são iguais'.format(n1, n2))
        
    elif opção == 4:
        print('Informe novos números ?')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('programa finalizado! ')  
    else:
        print('Opção inválida. Tente novamente')
    print('==+' * 10)
print('Fim do programa ! Volte sempre!')

#correção
# n1 = int(input('Primeiro Valor: '))
# n2 = int(input('Segundo Valor: '))
# opção = 0
# while opção != 5:
#     print(''' 
#     [ 1 ] somar
#     [ 2 ] multiplicar
#     [ 3 ] maior
#     [ 4 ] novos números
#     [ 5 ] sair do programa''')

#     opção = int(input('Qual é a sua opção? '))
#     if opção == 1:
#         print('SOMA!')
#         soma = n1 + n2
#         print('A soma entre {} e {} é {}'.format(n1,n2,soma))
#     elif opção == 2:
#         print('MULTIPLICAÇÃO')
#         produto = n1 * n2
#         print('O resultado de {} X {} é {}'.format(n1, n2, produto))
#     elif opção == 3:
#         if n1 > n2:
#             maior = n1
#         else:
#             maior = n2
#         print('Entre {} e {} maior valor é {}'.format(n1, n2, maior))
#     elif opção == 4:
#         print('Informe os números novamente: ')
#         n1 = int(input('Primeiro valor:'))
#         n2 = int(input('Segundo valor: '))
#     elif opção == 5:
#         print('Finalizando...')
#     else:
#         print('Opção inválida. Tente novamente')
#     print('*=' * 10)   
# print('Fim do programa! Volte sempre!')