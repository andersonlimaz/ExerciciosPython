#faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionario 
# com as seguintes informações:
#Quantidade de notas
#A maior nota
#A menor nota 
#A média da turma 
#A situação (opcional)

#Adicione também as docstrings da função. 
def notas(*n, sit=False):

    resp = 0
#Programa Principal 
resp = notas(5.5, 2.5, 9, 8.5)
print(resp)