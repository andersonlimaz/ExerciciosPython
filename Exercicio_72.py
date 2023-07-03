#CRIE UM PROGRAMA QUE TENHA UM TUPLA TOTALMENTE PREENCHIDA COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE.
#SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO. 
numeração = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))

    if 0 <= num <= 20:
        print(f'Você digitou o número {numeração[num]}')
    else:
        print('Número inválido. Tente novamente.')

    resp = input('Deseja continuar? [S/N] ').strip().upper()
    if resp != 'S':
        break

print('Obrigado, volte sempre!')

    
