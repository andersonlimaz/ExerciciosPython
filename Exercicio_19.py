#Um professor quer sotear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido. 
import random 
aluno1 = str(input('Qual o nome do primeiro aluno ?'))
aluno2 = str(input('Qual o nome do segundo aluno ?'))
aluno3 = str(input('Qual o nome do terceiro aluno ?'))
aluno4 = str(input('Qual o nome do quarto aluno ?'))
alunos= [aluno1,aluno2,aluno3,aluno4]

aluno_escolhido = random.choice(alunos)

print('O aluno escolhido para apagar quadro foi {}'.format(aluno_escolhido)) 