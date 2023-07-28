#faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionario 
# com as seguintes informações:
#Quantidade de notas
#A maior nota
#A menor nota 
#A média da turma 
#A situação (opcional)

#Adicione também as docstrings da função. 
def notas(*n, sit=False):
    """
    => função para analisar notas e situção dos alunos
    :param n: uma mais notas dos alunos(aceita varias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situção  
    :return: dicionario com vairas informações sobre a situação da turma. 
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
           r['situação'] = 'BOA'
        elif r ['média'] >=5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'   
    return r

#Programa Principal 
resp = notas(5, 5, 1, sit=True)
print(resp)
