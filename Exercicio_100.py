#faça um programa que tenha uma lista chama números e duas funções chamdas sorteia() e somaPar().
#A primeira função vai sortear 5 númeors e vai coloca-los dentro da lista e a segunda função vai
#Mostrar a soma entre todos os valores PARES sorteados pela função anterior. 
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n= randint(1, 10)
        lista.append(n)
        list.append
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto!')
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)