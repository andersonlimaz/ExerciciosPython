#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade 
#e a quantidade de dias pelos quais ele foi alugado. calcule o preço a pagar. sabendo que o carro custa R$60
#por dia e R$0.15 por km rodado

k=float(input('informe a quantidade de KM foi percorridas pelo carro: '))
d=int(input('informe a quantidade de dias que foi alugado o carro: '))
kr= k * 0.15
dr= d * 60 
resul= kr + dr
print('Portando o valor a pagar pelos KM R${:.2f} valor a pagar pelos dias R${:.2f} valor total R${:.2f}'.format(kr,dr,resul))

#correção 

dias= int(input('Quantos dias alugados? '))
km= float(input('Quantos Km rodados? '))
pago = dias * 60 +(km * 0.15)
print('O total a pagar é de R{:.2f}'.format(pago))
    