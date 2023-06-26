# crie um programa que leia vários numeros inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que pe a condição de para. No final, mostre quantos números foram digitados 
# e qual a soma entre ele (desconsiderando o flag). 

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))