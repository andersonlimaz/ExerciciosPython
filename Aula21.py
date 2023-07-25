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

def teste():
    x= 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Programa Principal 
n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}')