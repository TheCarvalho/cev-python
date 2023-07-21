# **EXE_115**

# > Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de texte simples. O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from os import system

from lib.arquivo import *
from lib.interface import *

arq = 'arquivo.txt'

# print(os.getcwd())  # para ver da onde o programa tá sendo rodado
# parece que quando vc abre uma workspace o python executa de lá e n da pasta onde está seu arquivo por isso ele salva os arquivos na workspace
if not arquivoexiste(arq):
    criararquivo(arq)


while True:
    system('cls')
    resposta = menu([
        'Ver pessoas cadastradas',
        'Cadastrar nova pessoa',
        'Sair do sistema'
    ])

    system('cls')

    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema...')
        sleep(2)
        quit()
    else:
        print('\033[1;31mERRO! Digite uma opção válida \033[m')
        sleep(1)
