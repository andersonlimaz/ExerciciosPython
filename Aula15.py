# cont = 1 
# while True: # executa estrutura para sempre. 
#     print(cont, ' ', end='')
#     cont += 1
# print('Acabou')

# # exemplo 2
# n = cont = 0
# while cont <3 :
#     n= int(input('Digite um número: '))
#     cont += 1
# exemplo 3
# n = s = 0
# while n != 999:
#     n = int(input('Digite um número: '))
#     s += n
# print('A soma vale {}'.format(s))

# exemplo 4

# n = s = 0
# while True:
#     n = int(input('Digite um número: '))
#     if n == 999:
#         break
#     s += n
# print('A soma vale {}'.format(s))

# forma de escrever f strings 
# s = 0
# print(f'A soma vale {s}')
nome = 'josé' 
idade = 33 
print(f'O {nome} tem {idade} anos. ') #Python 3.6+
print('O {} tem {} anos'.format(nome, idade)) #Python 3