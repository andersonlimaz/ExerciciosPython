#() tupla
#[] lista
#{} dicionario


# lanche = ('humburguer', 'Suco','Pizza', 'Pudim' )
# print(lanche[2:])



#tuplas são imutáveis
# lanche[1] = 'refrigetante'
# print(lanche[1])
#erro ocorre porque estamos tentando atribui valores a tupla. 

#primeira maneira de execução
# lanche = ('humburguer', 'Suco','Pizza', 'Pudim' )
# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Comi para caramba')

#segunda maneira de execução, mostra a posição. 
# lanche = ('humburguer', 'Suco','Pizza', 'Pudim', 'batata frita' )
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]}')
# print('comi para caramba')

# a = (2, 5, 4)
# b = (5,8,1,2)
# c = a + b
# print(c)

#imprime dados diferentes
pessoa = ('Anderson', 26, 'M', 99.88)
print(pessoa)