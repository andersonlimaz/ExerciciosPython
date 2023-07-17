# pessoas = {'nome':'Gustavo', 'sexo': 'M', 'idade':22}
# print(pessoas['idade'])
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# print(pessoas.keys()) 
# print(pessoas.values())
# print(pessoas.items())

# for k in pessoas.keys():
#     print(k)

# for k in pessoas.values():
#     print(k)

# for k, v in pessoas.items():
#     print(f'{k} = {v}')

#apagando 
# del pessoas['sexo']
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

#modificando nome 
# pessoas['nome'] = 'Leandro'
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# Adicionando 
# pessoas['peso'] = 98.5
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

#Criando dicionario dentro de uma lista. 
# brasil = []
# estado1 = {'uf':'Rio de janeiro', 'sigla':'RJ'}
# estado2 = {'uf':'São Paulo', 'sigla':'SP'}
# brasil.append(estado1)
# brasil.append(estado2)

# print(estado1)
# print(estado2)
# print(brasil[0])

#outro exemplo usando metodo copy 
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
