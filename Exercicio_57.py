#FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES 'M' OU 'F'.
#CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO. 
sexo = str(input('Qual o seu sexo [F/M]: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Por favor digite um [M/F]')
    sexo = str(input('Qual o seu sexo [F/M]: ')).upper()
