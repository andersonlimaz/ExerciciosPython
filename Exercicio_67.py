# #faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo usuário. 
# #O programa será interrompido quando o número solicitado for negativo. 
# print('*' *20)
# print('Tabuada')
# print('*'* 20)
# while True:
#     valor = int(input('Qual o Valor que deseja calcular? '))
#     print('para sair digite um valor negativo!')
#     print('='*20)
#     if valor < 0:
#         break
#     i = 1
#     while i <= 10:
#         resul = i * valor
#         print (f'{i} X {valor} = {resul}')
#         i += 1
# print('Programa encerrado!')

#correção 
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n <0:
        break
    print('-' * 30)
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
    print('-' * 30)
print('Programa tabuada encerrado. Volte sempre!')