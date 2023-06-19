#Pratica 
#Feito usando for in 
'''for c in range(1, 10):
    print(c)
print('fim')'''

#exemplo como como seria escrito em While
#while é ultilizado para quando você não sabe o limite.
c = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')
#outro exemplo 
for c in range(1,5):
    n = int(input('Digite um valor: '))
print('Fim')
#Usando um exemplo que não sabemos o final, quando for digitado o 0 o programa para
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

# exemplo utilizado a resposta se quer continuar. 
r = 'S'
while r == 'S':
    n= int(input('Digite um valor:'))
    r = str(input('Quer continuar ? [S/N]')).upper()
print('Fim')

#novo exemplo
n = 1
par = impar = 0
while n !=0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par +=1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares'.format(par, impar))