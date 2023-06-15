#faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 
número = int(input('Digite um número: '))
tot = 0
for c in range(1, número + 1):
    if número % c == 0:
        print('\33[33m', end=' ')
        tot += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
print('- O número {} foi divisível {} vezes'.format(número, tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('Por isso ele NÃO é primo')