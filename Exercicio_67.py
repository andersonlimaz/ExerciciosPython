#faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número solicitado for negativo. 
print('*' *20)
print('Tabuada')
print('*'* 20)
while True:
    valor = int(input('Qual o Valor que deseja calcular? '))
    print('para sair digite um valor negativo!')
    if valor < 0:
        break
    i = 1
    while i <= 10:
        resul = i * valor
        print (f'{i} X {valor} = {resul}')
        i += 1
print('Programa encerrado!')