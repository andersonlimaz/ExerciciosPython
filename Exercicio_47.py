#crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50. 
for c in range(0, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('Números Pares')
#outra forma de fazer economizando o números de laços é 
for n in range(2, 51, 2): #primeiro numero indica começo, segundo fim, terceiro de quando em quando vai pular. 
    print(n, end=' ')
print('Números Pares')