import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, (raiz)))
#exemplo 2
from math import sqrt
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, (raiz)))
#exemplo 3 
from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

