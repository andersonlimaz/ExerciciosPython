#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario 
#se por acaso a ctps for diferente de zero, o dicionario receberá também o ano de contratação e o salario. calcule e acrescente,
#alem da idade, com quantos anos a pessoa vai se aposentar. 
from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome:'))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('carteira de trabalho (0 não tem)'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano da contratação: '))
    dados['salario'] = float(input('Salario R$: '))
    dados['aposetadoria'] = dados['idade'] + (( dados['contratação'] + 35) - datetime.now().year)
print('*'*30)
print(dados)
for k, v in dados.items():
    print(f'  -{k} tem o valor {v}')