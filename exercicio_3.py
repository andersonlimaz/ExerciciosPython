#precisa colocar int, se não ele faz a concatenação. 
n1=int(input('digite um numero ? '))
n2=int(input('digite um numero ? '))
s=n1+n2 
print('A soma vale: ',s )
#faça aparecer a soma entre n1 e n2 vale = s 
n1=int(input('digite um numero ? '))
n2=int(input('digite um numero ? '))
s=n1+n2 
#print('A soma entre: ',n1, 'e',n2, 'vale',s )
#usando o .format 
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
