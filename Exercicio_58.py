#MELHORE O JOGO DO DESAFIO 028 ONDE O COMPUTADOR VAI "PENSAR" EM UM NUMERO ENTRE 0 E 10.
#SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, 
#MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSARIOS PARA VENCER.
  
from random import randint
from time import sleep
comp = randint(0, 10) 
print(''' 
Sou computador, pensei em um número de 0 e 10
Em qual número eu pensei ??? ''')
acertou = False
while not acertou :# while not acertou:: Inicia um loop que continuará até que o jogador acerte o número.
    jog = int(input('Qual o seu papite ?'))
    palpite = palpite + 1
    if jog == comp:
        acertou = True
    else:
        if jog < comp :
            print('tente novamente o número é MAIOR')
        elif jog > comp:
            print('tente novamente o número é MENOR')
print('Acertou com {}tentativas, Parabéns'.format(palpite))

#----------------------------------- 
from random import randint
from time import sleep
computador = randint(0, 10) # Sorteia o numero
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')#print informações do começo
acertou = False # declarada como falsa
palpites = 0 #contabilizar o numero iniciando por zero
while not acertou: # começa negando o palpite
    jogador = int(input('Qual é seu palpite: '))#ela vai perguntar o palpite enquanto você não acertar
    palpites += 1 #soma a palpite
    if jogador == computador: #quando jogador que é palpite for igual ao que o computador random colocou,  
        acertou = True #se caso for verdade ele sai do while. 
    else:
        if jogador < computador: # numero do jogador for menor que computador imprima "MAIS"
            print('Mais... tente mais uma vez.')
        elif jogador > computador:# número do jogador for maior que computador imprima "MENOS"
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas, Parabéns'.format(palpites))

