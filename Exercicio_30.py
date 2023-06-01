#crie um programa que leia um numero intero qualquer e mostre se ele é par ou impar. 
n = int(input('Digite um número qualquer: '))
resultado = n % 2
if resultado == 1:
    print('O numero digitado foi {} ele é um número IMPAR'.format(n))
else:
    resultado == 0 
    print('O numero digitado foi {} ele é um número PAR'.format(n))
print('O resultado foi {}'.format(resultado))