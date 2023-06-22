#MELHORE O DESAFIO 61, PERGUNTANDO PARA USUÁRIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS. O PROGRAMA ENCERRA QUANDO ELE DISSER QUE QUER MOSTRAR OS TERMOS. 
print('Gerador de Pa')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro 
cont = 1 
total = 0
mais = 10 # programa começa mostrando 10 termos  
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))