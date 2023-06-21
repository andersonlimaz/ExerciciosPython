#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL. 
# EX: 5! 5 X 4 X 3 X 2 X 1 = 120

n = int(input('''
Digite um numero 
Calcular o seu fatorial:'''))
c = n
print('Calculando {}! ='.format(n), end='')
f= 1
while c > 0:
    print(' {} '.format(c), end='')
    print(' X 'if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1

print('{}'.format(f))

#fazendo o mesmo programa com for
n = int(input("Digite um número para calcular o seu fatorial: "))
fact = 1

for i in range(1, n+1):
    fact *= i

print(f"O fatorial de {n} é {fact}.")
