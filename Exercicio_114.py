'''
<<<<<<< HEAD
Crie um codigo python que teste se site pudim esta acessivel pelo computador usado . 
'''   
=======
Crie um codigo python que teste se site pudim esta acessivel pelo computador usado. 
'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site pudim não está acessivel no momento')
else:
    print('Consegui acessar o site')
>>>>>>> e658f51994271961c5fc2b827006c068121cc9b5
