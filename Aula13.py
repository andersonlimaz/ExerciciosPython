#para escrever o print 6 vezes 
#usamos de 0 até 6 por que o ultimo numero ele ignora
for c in range(0,6):
    print('oi') #tudo que esta dentro do tab é repetido. 
print('fim')
#caso no lugar de ('oi') substituirmos por c, ele apresenta o numero
for c in range(0,6):
    print(c)
print('fim')
#caso quiser contar de frente para tras 
for c in range(6, 0 -1):
    print(c)
print('fim')
#lendo valor e usando dentro do for 
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')
# imprime uma sequência de números a partir do número de início até o número de fim, com o intervalo determinado pelo passo.
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p ):
    print(c)
print('Fim')
# vai repetir o digite um valor 3x 
for c in range(0, 3):
    n = int(input('digite um valor: '))
print('fim')
# vai repetir o digite um valor 4x, com somatorio 
s = 0 
for c in range(0, 3):
    n = int(input('digite um valor: '))
    s += n
print('O somatorio de todos os valores foi {}'.format(s))
