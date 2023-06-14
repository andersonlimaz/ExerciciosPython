#Crie um programa que faça o computador jogar JOKENPÔ com você. 
from random import randint
from time import sleep
print('======== JOKENPÔ do ANDERSÃO ==========')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')
jogador = int(input('Qual é sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

print('==+' *10)
print('computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('==+' *10)


if computador == 0: # Jogou pedra

    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:   
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:# Jogou papel

    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:   
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador ==2: # Jogou tesoura

    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:   
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')