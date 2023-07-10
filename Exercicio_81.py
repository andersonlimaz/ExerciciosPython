#Crie um programa que vai ler varios números e colocar em uma lista depois disso mostre:
#A- Quantos números foram digitados. 
#B- A lista de valores, ordenada de forma decrecente. 
#C- Se o valor 5 foi digitado e está ou não na lista. 
# valores = []
# cont = 0
# while True:
#     valores.append(int(input('Digite um valor: ')))
#     cont +=1
#     valores.sort(reverse=True)
#     sair = str(input('Quer continuar ? [S/N]')).upper().split()[0]
#     if sair == 'N':
#         break
    
# print(f'A lista de números digitados foi {valores} o número total de números foi {cont}')
valores = []
while True:
    valores.append(int(input('Digite o valor: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('*' *30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem descrecente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')