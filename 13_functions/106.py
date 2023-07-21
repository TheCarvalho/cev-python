# ### **EXE_106**

# > Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digirar a palavra **"FIM"**, o programa se encerrará.
def funcao():
    while True:
        comando = str(input('Insira o comando: ("FIM" para sair) ')
                      ).strip().lower()
        if comando == 'fim':
            print('Saindo..')
            quit()
        print(help(comando))


funcao()
