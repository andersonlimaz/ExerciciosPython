#Faça uma programa que tenha uma função chamada escreva(), 
#  que receba um texto qualquer como parametro e mostre uma mensagem com tamanho adaptavel. 
# ex: escreva ('Olá mundo! ')
# ----------------------- 
# Ola mundo!
# # --------------------------
# def escreva(txt):
#     tamanho = len(txt) 
#     print('~' * tamanho)
#     print(txt)
#     print('~' * tamanho)

# escreva(str(input('Mensagem: ')))

# ------------------correção
def escreva (msg):
    tam = len(msg) + 4
    print('^' * tam)
    print(f'  {msg}')
    print('^' * tam)


# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CEV')