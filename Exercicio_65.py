# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUÇÃO, MOSTRE O MÉDIA ENTRE E O MENOR VALORES LIDOS. 
# O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES. 
resp = 'S'
soma = quant = media = maior = menor = 0 
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 
    resp = str(input('Quer continuar: [S/N]')).upper().strip() [0]
media = soma / quant
print('Você digitou {} numeros e a media foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))