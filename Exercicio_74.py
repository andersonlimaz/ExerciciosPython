#CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA. 
#DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA. 
from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10),)
print('Os valores sorteados foram: ',end='')
for n in num:
    print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(num)}')  
print(f'O menor valor soreteado foi {min(num)}') 
