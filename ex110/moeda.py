def aumentar(preço=0, taxa=0, formato=False ):
    """
    -> Calcula o aumento de um determinado preço, 
    retornando o resultado com ou sem formatação, 
    param preço: o preço que se quer reajustar
    param taca: qual é a porcetagem do aumento. 
    param formato: quer a saida formatada ou nao?
    return: o valor reajustado, com ou sem formato
    """
    res = preço + (preço * taxa/100)
    return res if formato == False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço *taxa/100)
    return res if formato == False else moeda(res)
    

def dobro(preço=0,formato=False):
    res = preço * 2
    return res if formato == False else moeda(res)


def metade(preço=0, formato= False):
    res = preço /2 
    return res if format == False else moeda(res)

def moeda(preço=0, moeda = 'R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.',',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('^'*30)
    print('Resumo do valor'.center(30))
    print('^' * 30)
    print(f'Preço analisado: \t{moeda(preço)}' )
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'com {taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('^' * 30)