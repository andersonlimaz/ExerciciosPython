#refaça o desafio 09, mostrando a tabuada de um número que o usuário, só que agora ultilizando um laço for. 
cont = 0
print('********Tabuada*********')
num = int(input('Digite um número: '))
for c in range(1, 11):
    resul = num * c
    cont += 1 #cont = cont + 1 
    print('{} X {} = {}'.format(cont,num,resul))

#correção 
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1,11):
    print('{} X {:2} = {}'.format(c, num, num*c)) 