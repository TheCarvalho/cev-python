
# ### **EXE_105**

# > Faça um programa que tenha uma função notas() que pode recebar vários notas de alunos e vai retornar um dicionário com as seguintes informações:

# > - Quantidade de notas

# > - A Maior nota.
# > - A Menor nota.

# > - A Média da turma

# > - A Situação (opcional) Adicione também as docstrings.

def notas(*n, sit=False):

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit:
        if r['media'] < 7:
            r['situacao'] = 'Reprovado'
        else:
            r['situacao'] = 'Aprovado'

    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
