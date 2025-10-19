from time import sleep
from random import sample
quant = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = []
for c in range(0, quant):
    numeros = sorted(sample(range(1, 61), 6))
    jogos.append(numeros[:])
print('-='*3+f' SORTEANDO {quant} JOGOS '+'-='*3)
sleep(1)
for c in range(0, quant):
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(1)
print('-='*5+' < BOA SORTE > '+'-='*5)
