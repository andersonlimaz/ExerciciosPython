#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
valor=int(input('Digite o valor: '))
a = valor * 2
b = valor * 3 
c = valor ** (1/2)

print('O dobro é: {}\nO triplo é: {}\n A raiz Quadrada é: {}'.format(a,b,c))

#correção pelo prof do curso, o {:.2f} significa que vai pegar apenas dois numeros depois da virgula.
# para calcula a raiz quadrada também pode usar o pow(n, (1/2)).    
valor=int(input('Digite o valor: '))
print ('O dobro de {} vale {}.'.format(valor, (valor *2)))
print ('O triplo de {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(valor, (valor * 3), (valor ** (1/2))))
