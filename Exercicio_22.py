#Crie um progtam quer leia o nome completo de uma pessoa e mostre:
#1 O nome com todas minusculas 
#2 O nome com todas maiusculas
#3 Quantas letras ao todo (sem considerar espaços)
#4 quantas letras tem o primeiro nome. 

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('seu nome em Maiusculo é {}'.format(nome.upper()))
print('seus nome em Minisculas é {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))