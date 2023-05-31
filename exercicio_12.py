#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
produto=float(input('Informe o valor do produto?'))

a = produto * 5 / 100 
resultado = produto - a

print('O produto com 5 porcento de desconto {}'.format(resultado))

#correção 

preco=float(input('Qual é o preço do produto '))
novo = preco - (preco * 5 / 10 )
print('O produto que custava R${:.2f}, na promoção de 5% vai custar R${:.2f}'.format(preco, novo))