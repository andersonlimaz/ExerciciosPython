#CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS NA SEQUÊNCIA.
#NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR.
listagem = ('lapiz', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 20.32,
            'Mochila', 199.20,
            'Caneta', 1.90,
            'Livro', 15.98)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:-<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')        
print('-'*40)