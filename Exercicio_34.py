#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento
#para salario superiores a R$1.250,00, calcule um aumento de 10%.
#para os inferiores ou iguais, o aumento é de 15%
salario = float(input('Qual o salário do funcionario ? R$' ))
if salario <= 1250:
    ajuste = salario + (salario * 15 / 100)
else:
    ajuste = salario + (salario * 10 / 100 )
print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(salario, ajuste))