# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER NA TELA OS N PRIMEIROS ELEMENTOS DE UMA SEQUÊNCIA DE FIBONACCI. 
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~~' * 30 )
print('{} → {}'.format(t1,t2), end='')
cont = 3
while cont <= n:#enquanto contador foi menor ou igual a n que é o numero que foi inserido no começo. 
    t3 = t1 + t2
    print( ' → {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → Fim')