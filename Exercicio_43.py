#Descrevolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#entre 18.5 e 25: Peso ideal 
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida. 
peso = float(input('Informe o seu peso? (Kg) '))
altura = float(input('Informe sua altura? (m) '))
imc = peso / (altura ** 2)

print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está em Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está com Peso ideal, PARABÉNS!')
elif 25 <= imc < 30:
    print('Você está em Sobrepeso')
elif 30 <= imc < 40:
    print('Você está em Obesidade')
elif imc >= 40:
    print('Você está em Obesidade Mórbida, CUIDADO !')
