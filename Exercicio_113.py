'''
Reescreva a função leiaInt() que fizemos no exercicio 104, 
incluindo agora a possibilidade da digitação 
aproveite e crie também uma função leiaFloat() com a mesma funcionalidade. 
'''
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n= float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


#PRINCIPAL
n = leiaInt('Digite um número:')
print(f'Você acabou de digitar o número {n}')
