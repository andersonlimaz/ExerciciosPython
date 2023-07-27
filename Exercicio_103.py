#faça um programa que tenha uma função chamada ficha(), que rebe dois parametros opcionais:
#o nome de um jogador e quantos gols ele marcou 
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(jog='<Desconhecido>', gol= 0):
    print(f'O Jogador {jog} fez {gol} gol(s) no campeonato')


#programa principal 
n = str(input("Nome do jogador: "))
g = str(input("Numero de gols: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)