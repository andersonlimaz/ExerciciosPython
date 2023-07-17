#Faça um programa que leia nome e media de um aluno, guardado também a situação em um dicionario. 
#No Final mostre o conteudo da estutura na tela. 
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno ['media'] >= 7:
    aluno['situação'] ='Aprovado'
elif 5 <= aluno ['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('*'*30)
for k, v in aluno.items():
    print(f'  -{k} é igual a {v}')
