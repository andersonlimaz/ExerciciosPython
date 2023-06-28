#Crie um programa que leia o nome preço de varios produtos. o programa deverá perguntar se o usuário vai continuar. 
#no final, mostrar:
# qual é total gasto na compra
# quantos produtos custam mais de R$1000
# qual é o nome do produto mais barato.  

total_gasto = 0
produto_mais_1000 = 0
mais_barato = ''
preco_mais_barato = float('inf')

while True:
    nome_produto = input('Qual o nome do produto? ')
    preco_produto = float(input('Qual o preço do produto? '))
    total_gasto += preco_produto

    if preco_produto > 1000:
        produto_mais_1000 += 1
    
    if preco_produto < preco_mais_barato:
        mais_barato = nome_produto
        preco_mais_barato = preco_produto

    sair = input('Deseja cadastrar outro produto? [S/N]').upper().strip()

    if sair == 'N':
        break
print(f'Total gasto na compra: R${total_gasto:.2f}')
print(f'Quantidade de produtos que custam mais de R$1.000: {produto_mais_1000}')
print(f'Produtos mais barato: {mais_barato} - Preço: R${preco_mais_barato:.2f}')
    