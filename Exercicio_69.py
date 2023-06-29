# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
# o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
#A- quantas pessoas tem mais de 18 anos.
#B- Quantos homens foram cadastrados. 
#C - Quantas mulheres tem menos de 20 anos. 
# maior_18 = 0
# homens = 0
# Mulher_menos_20 = 0

# while True:
#     nome = str(input('Qual o seu nome: '))
#     idade = int(input('Qual a sua idade: '))
#     sexo = str(input('Qual seu sexo: [M/F] ')).upper().strip()
#     sair = str(input('Deseja cadastrar outra pessoa? [S/N]')).upper().strip()
 
#     if sexo == 'F' and idade < 20:
#         Mulher_menos_20 =+ 1

#     elif sexo == 'M':
#         homens += 1

#     elif idade <= 18:
#         maior_18 += 1

#     if sair == 'N':
#         break 

# print(f'Pessoas tem mais de 18 anos {maior_18}')
# print(f'Quantidade de homens cadastrados {homens}')
# print(f'Quantidade de mulhures te menos de 20 anos {Mulher_menos_20}')
  
#correção 
tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade:'))

    sexo = ' '
    while sexo not in 'MF':# enquanto o sexo não for MF, não vai passar, necessario declarar como vazio  
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    if idade >= 18:
        tot18 +=1

    if sexo == 'M':
        totH += 1

    if sexo == 'F' and idade < 20:
        totM20 += 1 

    resp = ' '
    while resp not in 'SN':
        resp= str(input('Quer continuar? [S/N]')).strip().upper()[0] #enquanto a resposta for S N, vai continuar perguntando
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')