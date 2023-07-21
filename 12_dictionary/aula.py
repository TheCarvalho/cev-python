
# * Anotações que fiz durante aula de dicionarios

'''a = tuple()
b = list()


# append n funcina no dicionario

x = str(input('Vai: '))
y = str(input('Outra: '))

c[x] = y
x = str(input('Vai: '))
y = str(input('Outra: '))
c[x] = y

print(c[1])

# del(c[x])
'''
#c = dict()
filme = {
    'titulo': 'star wars',
    'ano': '1977',
    'diretor': 'George Lucas'

}
# dicionario só referenciado pelo nome da keys e não pelos numeros obrigatoriamente como lista e tuplas
# filme.values() - valor dentro das keys
# filme.keys() - "categoria"/aquilo que armazena o valor
# filme.items() - values e keys

for k, v in filme.items():
    print(f'O {k} é {v}')

# n tem enumerete para dicionario(tuplas e listas) no dicionario tem que usar o items como no exemplo acima

# posso só adicionar
filme['rate'] = 'mto ruim'

estado['uf'] = str(input('Insira o estado: '))

brasil.append(estado.copy()) << para copiar, aquele[:] n funciona em dicionario
