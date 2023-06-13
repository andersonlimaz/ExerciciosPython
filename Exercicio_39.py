#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#se ele ainda vai se alistar ao serviço militar. 
#se é hora de se alistar
#Se já passou tempo do alistamento. 
#seu programa também devera mostrar o tempo que falta ou que passou do prazo. 
from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
sexo = str(input('Informe seu sexo, M = masculino e F = feminino: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if sexo.lower() == 'f':
    print('Sexo feminino não precisa fazer alistamento')
    exit()

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos '.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))