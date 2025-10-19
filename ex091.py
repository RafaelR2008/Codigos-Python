from operator import itemgetter
from random import randint
from time import sleep
jogadas = {'Jogador1': randint(1, 6),'Jogador2': randint(1, 6),
           'Jogador3': randint(1, 6),'Jogador4': randint(1, 6)}
print('Valores sorteados: ')
for k, v in jogadas.items():
    print(f'    O {k} tirou {v} no dado.')
    sleep(1)
print('Ranking dos jogadores: ')
jogadas = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
cont = 1
for k, v in jogadas:
    print(f'{cont}º lugar: {k} com {v} no dado.')
    cont += 1
    sleep(1)
