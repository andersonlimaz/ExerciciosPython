#faça um programa que leia a largura e a altura de um parece em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta, pinta uma ara de 2m². 

largura=float(input('Informe a largura da parece ? '))
altura=float(input('Informe a altura da parede ? '))

resultado = largura * altura
tinta = resultado /2
print('Largura informada: {}\nAltura informada: {}\nPortanto sua area é {}m²\nÉ necessario {}L de tinta. '.format(largura,altura,resultado,tinta))

#Correção 
larg= float(input('Largura da parede: '))
alt= float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}X{}e sua area é de {}m³'.format(larg, alt, area))
tinta = area / 2 
print('para pintar a parede, você precisara de {}l de tinta'.format(tinta))



