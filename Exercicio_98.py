#faça um programa que tenha a função contador(), que receba tres parametros:inicio, fim e passo e realize a contagem. 
# seu programa tem que realizar trs contagens atraves da função criada:
# A - de 1 até 10, de 1 em 1
# B - de 10 até 0, de 2 em 2
# C - personalizada
def contador(i, f, p):
    print(f'contagem de {i} até {f} de {p} em {p}')

    cont = i
    while cont <=f:
        print(f'{cont} ', end='' )
        cont += p
    print('FIM!')

#Programa Principal 
contador(1, 10, 1)
