#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
#À vista dinheiro/cheque : 10% de desconto
#À vista no cartão: 5% de desconto 
#em até 2x no cartão: preço normal 
#3x ou mais no cartão 20% de juros. 

print('============= Lojas Lima =============')
preço = float(input('Preço das Compras: R$'))
des1 = preço - (preço * 10/100)
des2 = preço - (preço * 5/100)

print('''Informe a forma de pagamento:
[1] PAGAMENTO Á VISTA COM 10% DESCONTO
[2] PAGAMENTO Á VISTA NO CARTÃO COM 5% DESCONTO
[3] PAGAMENTO PARCELADO, EM ATÉ 2X PREÇO NORMAL
[4] PAGAMENTO EM MAIS DE 2X 20% DE JUROS''')
opção = float(input('QUAL É SUA OPÇÃO: '))

if opção == 1: 
    print('Pagamento a vista R${:.2f} com desconto 10% valor passa a ser R${:.2f}'.format(preço, des1))
elif opção == 2:
    print('Pagamento á vista no cartão R${:.2f} com desconto de 5% R${:.2f}'.format(preço, des2))
elif opção == 3:
    parc2 = preço / 2
    print('Pagamento em 2x no cartão, SEM JUROS R${:.2f} 2x R${:.2f}'.format(preço, parc2))
elif opção == 4:
    parc =int(input('Quantas parcelas ?'))
    des4 = preço + (preço * 20/100)
    totalparc = des4 / parc
    print('Sua compra parcelada em {}x valor de R${:.2f} por parcela'.format(parc, totalparc))
    print('Pagamento em mais 2x valor R${:.2f} sua compra no final vai custar R${:.2f}'.format(preço, des4))
    
