#Escreva um programa que leia dois números inteiros e compare-os monstrando na tela a mensagem:
#O primeiro valor é maior 
#o segundo valor é maior 
#não existe valor maior, os dois são iguais 
n1 = int(input('Escreva o primeiro número: '))
n2 = int(input('Escreva o segundo número: '))

if n1 > n2:
    print('O PRIMEIRO é maior !')
elif n2 > n1:
    print('O SEGUNDO é maior !')
elif n1 == n2:
    print('não existe valor maior, os dois são iguais ! ')
