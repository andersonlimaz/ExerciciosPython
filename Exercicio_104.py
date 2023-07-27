#Crie um programa que tenha a função leialnt(), que vai funcionar de forma semelhante á função input do Python,
#Só que fazendo a validação para aceitar apenas um valor numérico. 
#EX n = leialnt('Digite um n ')
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m ')
        if ok:
            break
    return valor

#PRINCIPAL
n = leiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}')
