#Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada 
n=int(input('Digite um numero ? '))

n1 = n*1
n2 = n*2
n3 = n*3
n4 = n*4
n5 = n*5
n6 = n*6
n7 = n*7
n8 = n*8
n9 = n*9
n10 = n*10

print('A tabuada do numero {}: \n1 X {}\n2 X {}\n3 X {}\n4 X {}\n5 X {}\n6 X {}\n7 X {}\n8 X {}\n9 X {}\n10 X {}'.format(n,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10))

#correção 
num= int(input('Digite um numero para ver sua tabuada ? '))
print('-' * 12)
print('{} X {:2} = {}'.format(num, 1, num*1))
print('{} X {:2} = {}'.format(num, 2, num*2))
print('{} X {:2} = {}'.format(num, 3, num*3))
print('{} X {:2} = {}'.format(num, 4, num*4))
print('{} X {:2} = {}'.format(num, 5, num*5))
print('{} X {:2} = {}'.format(num, 6, num*6))
print('{} X {:2} = {}'.format(num, 7, num*7))
print('{} X {:2} = {}'.format(num, 8, num*8))
print('{} X {:2} = {}'.format(num, 9, num*9))
print('{} X {:2} = {}'.format(num, 10, num*10))
print('-' * 12)