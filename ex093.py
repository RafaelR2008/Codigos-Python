jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
quant = int(input('Quantas partidas ele jogou? '))
listgols = []
for c in range(0, quant):
   listgols.append(int(input(f'Quantos gols na partida {c+1}? ')))
jogador['gols'] = listgols[:]
jogador['total'] = sum(listgols)
print('-=' * 30)
for k, v in jogador.items():
    print(f'A chave {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador['nome']} jogou {quant} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {sum(listgols)} gols.')
