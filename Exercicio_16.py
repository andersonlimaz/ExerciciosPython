#crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira. 
'''from math import trunc
real = float(input('Digite um valor ?'))

print("O valor digitado foi {} e a porção inteira é {}".format(real, trunc(real)))'''

#segunda forma de fazer esse mesmo programa 

num = float(input('digite o valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num) ))