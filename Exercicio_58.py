#MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI "PENSAR" EM UM NUMERO ENTRE 0 E 10.
#SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, 
#MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSARIOS PARA VENCER.
 
from random import randint
from time import sleep
computador = randint(0, 10) # Sorteia o numero
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
