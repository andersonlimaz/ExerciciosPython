from interface import *
from time  import sleep
from sistema import *

arq = 'curso em video.txt'

if arquivoExiste(arq):
    

while True:
    resposta = menu(['Ver Pessoas cadastradas','Cadastrar nova Pessoas','Sair do sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro! digite uma opção valida\033[m')
    sleep(2)