# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro:
#     print(f'Problema encontrado foi {erro.__class__}')
# else:
#     print(f'O resultado é {r}')
# finally:
#     print('Volte sempre, Muito Obrigado!')
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de daos que você digitou')
except ZeroDivisionError:
    print('Não foi possivel dividir o valor por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre, Muito Obrigado!')