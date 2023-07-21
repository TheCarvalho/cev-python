
# from typing_extensions import runtime


try:  # lets you test a block of code for errors.
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):  # lets you handle the error.
    print('Tivemos um problema com os tipos de dados que vc digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: # lets you execute code when there is no error.
    print(f'O resultado é {r:.1f}')

finally:   # lets you execute code, regardless of the result of the try- and except blocks
    print('Volte sempre! Muito Obrigado!')

# * Alguns tipos de erros:
'''
NameError
ValueError
ZeroDivisionError
TypeError
IndexError
KeyError
EOFError
KeyboardInterrupt
OSError
MemoryError
ConnectionError
RuntimeError
'''
