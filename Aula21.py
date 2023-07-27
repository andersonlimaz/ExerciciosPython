# help(print)
# print(input.__doc__)
# ---------------------------
# def contador(i, f, p):

#     c = i
#     while c <= f:
#         print(f'{c}', end='')
#         c += p
#     print('Fim!')

# contador(2,10,2)

# =========================
#parametro opcional. 
# def somar(a = 0, b = 0, c = 0):
#         s = a + b + c
#         print(f'A soma vale {s}')

# somar(3, 2, 5)
# somar(8, 4)
# =====================
# Escopo de variaveis
# =======================

# def teste():
#     x= 8
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, x vale {x}')

# #Programa Principal 
# n = 2
# print(f'No programa principal, n vale {n}')
# teste()
# print(f'No programa principal, x vale {x}')
# ========================================
# parte pratica da aula

# def fatorial(num =1 ):
#     f = 1
#     for c in range(num, 0, -1):
#         f*=c
#     return f

# n= int(input('Digite um número: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}') 

# Outro exemplo 


# def fatorial(num =1 ):
#     f = 1
#     for c in range(num, 0, -1):
#         f*=c
#     return f
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2}, {f3}')

#Exemplo return valor logico 
def parOuImpar(n=0):
    if n % 2 == 0:
