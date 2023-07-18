#Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cadas pessoa em um dicionario e todos os dicionarios em uma lista
#No final, mostre:A- Quantas pessoas foram cadastradas 
#B - A média de idade do grupo
#C - Uma lista com todos as mulheres 
#D - Uma lista com todos as pessoas com idade acima da media. 
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por Favor, digite apenas [M/F].')
    pessoa['idade'] = int(input('idade: '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp =str(input('Deseja Continuar ? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda Apenas [S/N]')
    if resp == 'N':
            break
print('*'* 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A media de idade é de {media:2.0f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
print()
print('Lista das pessoas que estão acima da media: ',)
for p in galera:
     if p['idade']>= media:
            print('   ')
            for k, v in p.items():
                print(f' {k} = {v} ', end= '')
            print()
print('<<Encerrado>>')