#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o ususario tentar descobrir qual o numero escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu 
# print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')

# n = int(input('Em que número eu pensei ?'))
# if n == 0:
#     print('Você acertou parabens')
# else:
#     n != 0
#     print('Você errou, tente novamente! ')
#tentativa 
#---------------------------------------------------------------------------------------------------------
#correção 
from random import randint
from time import sleep
computador = randint(0, 5) # Sorteia o numero
print('-===' * 10)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
print('-===' * 10)
jogador = int(input('Em que número eu pensei ? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns você acertou, o numero que eu pensei foi o {}'.format(computador))
else:
    jogador != computador
    print('GANHEI, Eu pensei no número {} e você digitou {}'.format(computador, jogador))
