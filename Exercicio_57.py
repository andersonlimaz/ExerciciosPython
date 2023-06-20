#FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SÓ ACEITE OS VALORES 'M' OU 'F'.
#CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO. 
sexo = str(input('Qual o seu sexo [F/M]: ')).upper()
while sexo != 'M' and sexo != 'F':
    print('Dados inválidos. Por favor, informe seu sexo: [M/F] ')
    sexo = str(input('Qual o seu sexo [F/M]: ')).upper()

#correção 
  
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, infroem seu sexo: ')).strip().upper()[0]
print('Sexo {} registrados com sucesso'. format(sexo))