#Crie um programa que leia duas notas de um aluno e calcule a media, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: reprovado
#Média entre 5.0 e 6.9: recuperação 
#Média 7.0 ou superior: aprovado 

n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))
if media < 5.0:
    print('Média abaixo de 5.0: REPROVADO')
elif 7 > media >=5:
    print('Média entre 5.0 e 6.9: RECUPERAÇÃO ')
elif  media >= 7.0:
    print('Média 7.0 ou superior: aprovado') 