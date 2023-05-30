#faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
nome=input('qual o seu nome ?')
print('É um prazer te conhecer',nome)

#pode ser feito assim também, usando o .format para formatar espaço delimitado pelo {}.

nome=input('qual o seu nome?')
print('É um prazer te conhecer {}!'.format(nome))