#crie um programa que crie matriz de dimensão 3x3
#e preencha com valores lidos pelo teclado
matriz = [[],[],[],[],[],[],[],[],[]]
for i in range(0,9):
    matriz[i].append(int(input(f'Digite o {i} valor:')))
print(f'Matriz {matriz}')