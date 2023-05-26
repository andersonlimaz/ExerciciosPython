frase = 'Curso em Video Python  '
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])

#para imprimir texto grandes, abre aspas duas """ tres vezes como no ex abaixo 
print("""Eu vou me tornar um grande programador
serie bem sucesso, na minha vida em todos os setores
programar em python é muito bom""")

print(frase.count('o')) # tem diferença em maisculo e minisculo. 
print(frase.upper().count('O'))# contato quantidade de o, que se tornaram maisculas. 
print(len(frase))# espaços conta
print(len(frase.strip())) # strip remove espaços antes e depois. 
print(frase.replace('Python', 'Android'))# troca python por android 
print('Curso'in frase)
print(frase.find('Video'))# mostra a posição 
print(frase.split())# mostra a lista de palavras 