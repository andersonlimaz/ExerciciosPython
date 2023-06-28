# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
# o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
#A- quantas pessoas tem mais de 18 anos.
#B- Quantos homens foram cadastrados. 
#C - Quantas mulheres tem menos de 20 anos. 
maior_18 = 0
homens = 0
Mulher_menos_20 = 0

while True:
    nome = str(input('Qual o seu nome: '))
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('Qual seu sexo: [M/F] ')).upper().strip()
    sair = str(input('Deseja cadastrar outra pessoa? [S/N]')).upper().strip()
 
    if sexo == 'F' and idade < 20:
        Mulher_menos_20 =+ 1

    elif sexo == 'M':
        homens += 1

    elif idade <= 18:
        maior_18 += 1

    if sair == 'N':
        break 

print(f'Pessoas tem mais de 18 anos {maior_18}')
print(f'Quantidade de homens cadastrados {homens}')
print(f'Quantidade de mulhures te menos de 20 anos {Mulher_menos_20}')
  