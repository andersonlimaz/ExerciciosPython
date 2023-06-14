#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilaterio: Todos lados são igual 
#Isósceles: dois lados igual 
#Escaleno: todos os lados diferentes 
print('-+' * 10 )
print('Analisando triângulo')
print('-+' * 10 )

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')

if r1 == r2 == r3:
    print('Triângulo Equilatero')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Triângulo Esósceles')
else: 
    print('Triângulo Escaleno')
