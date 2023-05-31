#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento. 

salario=int(input('Informe o salario do Funcionario ?'))

a = salario * 15 / 100
resultado = salario + a

print('O salario anterior do funcionario era {} o salario atual com 15 porcento de aumento {}'.format(salario,resultado))

#correção 
salario = float(input('Qual é o salario do funcionario? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario,novo))