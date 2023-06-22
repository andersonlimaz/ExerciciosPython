#CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL,
#MOSTRE QUANTOS NÚMEROS FORMA DIGITADOS E QUAL FOI A SOMA ENTRE ELES (DESCONSIDERANDO O FLAG)
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: ')) #comando é passado anteriormente, para que quando abertar 999 o program encerre
while num != 999: 
    soma += num 
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('você digiou {} número e a soma entre eles foi {}'.format(cont, soma))
