#Faça um progrma que tenha uma função chamada area(), que receba as dimensões de um terreno retangular 
#(largura e comprimento) e mostre a área do terreno. 

def area(largura, comprimento):
    return largura * comprimento

largura = int(input('Informe a largura (m): '))
comprimento = int(input('Informe o comprimento (m): '))
resultado = area(largura, comprimento)
print(f'Com a largura {largura}m² e comprimento {comprimento}m², a área total é de {resultado}m²')
# --------------------------------------------correção


def arear(larg, comp):
    a= larg * comp
    print(f'A aréa de um terreno {larg}X{comp} é de {a}m²')

#programa principal
print('controle de Terrenos')
print('-'*20)
l = float(input('Lagura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)