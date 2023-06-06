#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa,
#O salario do comprador e em quantos anos ele vai pagar. 
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o empretimo sera negado. 

'''valor = float(input('Qual o valor da casa que deseja financiar: R$ '))
salario = float(input('Qual o seu salario: R$? '))
qts = int(input('Quantas vezes deseja pagar ? '))

prestacao = valor / qts
if prestacao <= (salario * 30 / 100):
    print('O emprestimo foi negado')
else:
    print('O emprestimo foi aprovado! ')'''

#Correção 

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Quantos anos de finaciamento: ')) 
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print ('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end=' ')
print('a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser Concedido!')
else:
    print('Emprestimo Negado!')    