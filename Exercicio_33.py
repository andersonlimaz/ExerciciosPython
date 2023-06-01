#faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor. 
n1 = int(input('informe o primeiro número: '))
n2 = int(input('informe o segundo número: '))
n3 = int(input('informe o terceiro número: '))

menor = n1 
if n2 < n1 and n2 < n3:
    menor = n2
if n3<n1 and n3 < n2:
    menor = n3
print('o menor valor digitado foi {}'.format(menor))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3>n1 and n3 > n2:
    maior = n3
print('O maior valor digitado foi {}'.format(maior))
