def ficha(n='<desconhecido>', g=0):
    return f'O jogador {n} fez {g} gol(s) no campo.'

nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: ')).strip()
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    print(ficha(g=gols))
else:
    print(ficha(nome, gols))
