#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar 
# R$ 1 dolar Usa R$ 3,27

Carteira=(float(input('informe quanto você tem de dinheiro na carteira ?')))

calculo = Carteira/3.27

print('Valor da sua carteira em reais é: {}\nO valor que você tem na sua carteira convertido em dolar é: {}'.format(Carteira,calculo))

#Correção 
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}.format(real, dolar)'.format(real,dolar))