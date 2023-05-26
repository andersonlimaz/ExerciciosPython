#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros 
conversor=int(input('Digite a quantidade de metros? '))

centimetros = conversor *100
milimetros = conversor *1000

print('A quantidade digitada foi: {}\nEm centimetros: {}\nEm milimetros: {}'.format(conversor,centimetros,milimetros))