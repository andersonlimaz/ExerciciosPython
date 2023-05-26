#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa. 

'''co = float(input("informe comprimento do cateto oposto: "))
ca = float(input("informe comprimento do adjacente: "))

hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}'.format(hi))'''

#outra maneira de fazer 
from math import hypot

co = float(input("informe comprimento do cateto oposto: "))
ca = float(input("informe comprimento do adjacente: "))
hi = hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))s