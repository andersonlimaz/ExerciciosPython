# # Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder,
# #mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
# from random import randint
# print('0-' *20)
# print('Vamos jogar IMPAR OU PAR')
# print('0-' *20)

# vitorias =0
# while True:
#     valor_jogador = int(input('Diga o valor? '))
#     escolha_jogador = str(input('Par ou IMPAR [P/I]: ')).strip().upper()

#     valor_comp = randint(1,10)
#     soma = valor_jogador + valor_comp

#     print(f'Você jogou {valor_jogador} e o computador jogou {valor_comp} o valor da soma é {soma}', end=' ')
#     print('DEU PAR!' if soma % 2 == 0 else 'DEU ÍMPAR!')

#     if (escolha_jogador == 'P' and soma % 2 == 0) or (escolha_jogador == 'I' and soma % 2 != 0):
#         print('Você VENCEU! ')
#         vitorias += 1
#     else:
#         print('Você Perdeu!')
#         break
# print(f'GAME OVER! Você conquistou {vitorias} vitoria(s) consecutiva(s)')

#correção 
from random import randint

v = 0
while True:
    jogador = int(input('Diga o valor: '))
    computador = randint(1,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in ('PpIi'):
        tipo = str(input('Par ou Ímpar: [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. total de {total}', end='')
    print(' DEU PAR' if total %2 == 0 else ' DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você PERDEU!')
            break
        print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {v} vezes')
    

