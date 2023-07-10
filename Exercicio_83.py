#crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
#Seu aplicativo deverá analisar se a expresãoo passada está comos parênteses abertos e fechados na ordem correta
expr = str(input('Digite a expressão '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta válida')
else:
    print('Sua expressão esta invalida')