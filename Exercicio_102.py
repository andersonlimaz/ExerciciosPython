#Crie um programa que tenha uma função fatorial() que receba dois parametros: o primeiro que indique o número
#a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se sera mostrado ou não 
#na tela o processo de calculo do fatorial
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número. 
    :Param n: O numero a ser calculado.
    :param Show: (opcional) Mostrar ou não a conta. 
    :return: O valor do fatorial de um número n. 
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c , end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

            
        f *= c
    return f

print(fatorial(5, show=True))
help(fatorial)