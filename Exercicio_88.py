#Faça um programa que ajude um jogador da mega sena a criar palpites. 
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. 
from random import randint
from time import sleep
lista = list()
jogos = list()

print('='*40)
print('     Joga na Mega Sena ')
print('='*40)

quant = int(input('Quantas vezes você quer que eu sorteie? '))
tot = 1

while tot <= quant:
    cont = 0
    lista.clear()

    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    tot += 1

print('*'*10, f'Sorteando {quant} Jogos', '*'*10)

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('*'*5,f'Boa sorte','*'*5)