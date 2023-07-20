
# * Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# *  a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

times = (
    'Palmeiras,',    'Flamengo,',    'Internacional,',    'Grêmio,',    'São Paulo,',    'Atlético-MG,',    'Athletico-PR,',    'Cruzeiro,',
    'Botafogo,',    'Santos,',    'Bahia,',    'Fluminense,',    'Corinthians,',    'Chapecoense,',    'Ceará,',    'Vasco,',
    'Sport,',    'América-MG,',    'Vitória,',    'Paraná,'
)

# print('Os 5 primeiros times: ', end='')
print('Os 5 primeiros times: ', *times[0:5])

print('Os ultimos 4 colocados: ', end='')
print(*times[-4:])

print('Em ordem alfabetica: ', end='')
print(*sorted(times))

print(f'Chapecoense está na posição: {times.index("Chapecoense,") + 1}')
