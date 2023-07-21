# print('-'*30)
# print('     Curso em video   ')
# print('-'*30)
# print('-'*30)
# print('     Aprenda Python  ')
# print('-'*30)
# print('-'*30)
# print('     Anderson Lima   ')
# print('*'*30)

# def lin():
#     print('-'*30)


# #Usando o def, função 
# lin()
# print('     Curso em video   ')
# lin()
# lin()
# print('     Aprenda Python  ')
# lin()
# lin()
# print('     Anderson Lima   ')
# lin()
 
# # ------------------------------
# def titulo(txt):
#     print('*' *30)
#     print(txt)
#     print('*'*30)

# titulo('    Curso em video  ')
# titulo('    Aprenda Python  ')
# titulo('    Anderson Lima   ')

# # --------------------------------------
# exemplo
# a = 4
# b = 5 
# s = a + b
# print(s)
# a = 8 
# b = 9 
# s = a + b 
# print(s)
# a = 2 
# b = 1 
# s = a + b 
# print(s)

# ------------- Ultizando def ---------------
# def soma(a, b):
#     s = a + b
#     print(s)


# #programa Principal
# soma(4, 5)
# soma(8, 9)
# soma(1, 2)

# # ---------------------------------
# def soma (a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')

# soma(b=4, a=5)
# soma(7, 10)


# ******************************************
# def contator(* num):
#     tam = len(num)
#     print(f'Recebi os valores{num} e são ao todo {tam} numeros')

# contator(1,2,3,3)
# contator(1,8)
# contator(4,4,4,4,2 )
# *******************************************
def dobra(lst):
    pos= 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)