#faça um programa que leia um numero interio e mostre na tela o seu sucessor e seu antecessor
valor=int(input('digite um numero ? '))
a= valor -1 
b= valor +1

print('O valor digitado foi: {}\nO valor do numero anterior é: {}\nO valor sucessor é: {}'.format(valor, a, b))

#Correção outro modo que pode ser feito 

n=int(input('digite um numero ? '))
print('Analisando o valor {}seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))