#Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores. 
#considere a maioridade 21 anos 
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior +=1
    else:
        totmenor +=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas maiores de idade'.format(totmenor))
