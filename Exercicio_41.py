#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,de acordo com a idade:
#até 9 anos: MIRIM 
#até 14 anos: Infantil 
#até 19 anos: JUNIOR
#até 20 anos: Sênior
#Acima: Master
from datetime import  date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
if idade <= 9:
    print('esse aluno tem {} anos, é da categoria MIRIM '.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos, é da categoria INFÂNTIL '.format(idade))
elif idade <=19:
    print('O atleta tem {} anos, é da categoria JUNIOR '.format(idade))
elif idade <=25:
    print('O atleta tem {} anos, é da categoria SÊNIOR '.format(idade))
else:
    print('O atleta tem {} anos, é da categoria MASTER '.format(idade))