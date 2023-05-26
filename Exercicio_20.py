#Professor pediu para que os alunos, sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
aluno1 = str(input('Qual o nome do primeiro aluno ?'))
aluno2 = str(input('Qual o nome do segundo aluno ?'))
aluno3 = str(input('Qual o nome do terceiro aluno ?'))
aluno4 = str(input('Qual o nome do quarto aluno ?'))
alunos= [aluno1,aluno2,aluno3,aluno4]
shuffle(alunos)

print('A ordem escolhida para apresentação do trabalho foi {}'.format(alunos))