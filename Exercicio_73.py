#CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPENATO BRASILEIRO DE FUTEBOL
#NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
#A-APENAS OS 5 PRIMEIROS COLOCADOS
#B-OS 4 ÚLTIMOS COLOCADOS DA TABELA
#C-UM LISTA COM OS TIMES EM ORDEM ALFABÉTICA
#D-EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DA CHAPECOENSE. 
times = ('Corinthians','Internacional','Fluminense','Flamengo','Athletico-PRA','tlético-MG','Fortaleza',
                 'América-MG','Botafogo','Santos','Goiás','Red Bull', 'Bragantino','Coritiba','Cuiabá','Ceara',
                 'Chapecoense','Avaí','Palmeiras','São Paulo')
print('*'*30)
print(f'Lista de times Brasileirão: {times}')
print('*'*30)
print(f'Os cinto primeiros colocados {times[0:5]}')
print('*'*30)
print(f'Os ultimos times são {times[16:]}')
print('*'*30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('*'*30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
