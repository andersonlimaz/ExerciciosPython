#dissecando uma variável
#faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele  
a=input('digite algo ?')
print('o tipo primitivo desse valor é', type(a))
print('Só tem espaços ?', a.isspace())
print('É um numero ?', a.isnumeric())
print('É alfabetico ?', a.isalpha())
print('É alfanumerico ?', a.isalnum())
print('Esta em maiúsculas?', a.isupper())
print('Esta em minusculas ?', a.islower ())
print('Está caputalizada?', a.istitle())