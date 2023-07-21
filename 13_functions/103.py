# ### **EXE_103**

# > Faça um programa que tenha uma função chamado ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador="desconhecido", gols=0):
    print(f'O jogador {jogador} marcou {gols} gol(s) no campeonato')


jogador = str(input('Insira o nome do jogador: ')).strip().title()
gols = str(input('Insira a quantidade de gols marcados pelo jogador: '))

if gols.isnumeric():  # ! isnumeric ou isalguma coisa parece que só funciona com string
    # ! Como eu iniciei como string para poder deixar vazia o input eu converto para int agora se ele for algum numero
    gols = int(gols)
else:
    gols = 0  # ! Se n tiver nenhum numero ele vira 0
if jogador.strip() == '':  # ! Checando que o nome do jogador está vazio
    # ! então apenas gols será importado para a função e o parametro gols lá na função já está como desconhecido como padrão
    ficha(gols=gols)
else:
    ficha(jogador, gols)  # ! se jogador n estiver vazio, ambos serão importados
