#desevolva um programa que pergunte a distancia de uma viagem em km. 
#calcule o preço da passagem, cobrando R$0,50 por Km para vigens de até 200km
# e R$ 0,45 para viagens mais longas. 

distancia = float(input('Qual a distância da viagem em KM? '))
print('Você esta prestes a começar uma viagem de {}KM '.format(distancia))
if distancia <= distancia:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))