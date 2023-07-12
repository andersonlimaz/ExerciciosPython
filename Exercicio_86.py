#crie um programa que crie matriz de dimensão 3x3
# #e preencha com valores lidos pelo teclado
# matriz = [[],[],[],[],[],[],[],[],[]]
# for i in range(0,9):
#     matriz[i].append(int(input(f'Digite o {i} valor:')))
# print(f'Matriz {matriz}')

matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-*'*90)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()