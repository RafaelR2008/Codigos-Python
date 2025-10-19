time = []
while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    quant = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    listgols = []
    tot = 0
    for c in range(0, quant):
       listgols.append(int(input(f'Quantos gols na partida {c+1}? ')))
       tot += listgols[c]
    jogador['gols'] = listgols[:]
    listgols.clear()
    jogador['total'] = tot
    time.append(jogador.copy())
    esc = input('Quer continuar? [S/N] ').strip().upper()
    while 'S' != esc != 'N':
        esc = input('Apenas S para sim ou N para não. Quer continuar? [S/N] ').strip().upper()
    if esc == 'N':
        break
    print('-'*40)
print('-=' * 30)
print(f'cod {'nome':<15}{'gols':<15} total')
print('-' * 40)
for i, j in enumerate(time):
    print(f'{i:>3} {j['nome']:<15}{str(j['gols']):<15} {j['total']}')
while True:
    print('-' * 40)
    esc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if esc == 999:
        break
    if esc >= len(time) or esc < 0:
        print(f'ERRO! Não existe jogador com código {esc}! Tente novamente.')
        continue
    print(f'-- LEVANTAMENTO DO JOGADOR {time[esc]["nome"].upper()}:')
    for i, g in enumerate(time[esc]["gols"]):
        print(f'No jogo {i+1} fez {g} gols.')
print('<< VOLTE SEMPRE >>')
