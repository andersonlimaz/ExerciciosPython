#Aprimore o desafio 093 para que ele funcione com vários jogadores,
#incluindo um sistema de visualizaçõa de detalhes do aproveitamento de cada jogador

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input(' Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ?  '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1} ? ')))
    jogador['gols'] = partidas[:]
    jogador['total']= sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar ? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N. ')
    if resp == 'N':
        break
print('*'*30)
print('cod ', end='' )
for i in jogador.keys():
    print(f' {i:<15} ', end='')
    
print('*'*30)
for k, v in enumerate(time):
    print(f' {k:>4} ', end='')
    for d in v.values():
        print(f' {str(d)} ')
print('*'*30)

