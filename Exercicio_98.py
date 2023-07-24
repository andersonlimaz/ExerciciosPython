#faça um programa que tenha a função contador(), que receba tres parametros:inicio, fim e passo e realize a contagem. 
# seu programa tem que realizar trs contagens atraves da função criada:
# A - de 1 até 10, de 1 em 1
# B - de 10 até 0, de 2 em 2
# C - personalizada
from time import sleep
def contador(i, f, p):
    print('^^' *20)
    print(f'contagem de {i} até {f} de {p} em {p}')
    sleep(0.2)
    
    if p < 0:
        p*= -1 
    if p == 0:
        p = 1

    if i < f: 
        cont = i
        while cont <=f:
            print(f'{cont} ', end='', flush=True )
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')
    
#Programa Principal
contador(1,10,1) 
contador(10,0,2)
print('^^' *20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio:  '))
fim = int(input('Fim:     '))
pas = int(input('Passo:   '))
contador(ini, fim, pas)