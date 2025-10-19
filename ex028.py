from random import randint
from time import sleep
print('-'*50)
print(f'{'JOGO: ADIVINHE O NÚMERO':=^50}')
print('-'*50)
rand = randint(0, 5)
print('Pensarei em um número entre 1 e 5, tente adivinhar!')
guess = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if rand == guess:
    print(f'Você acertou! O numero que eu estava pensando era de fato {rand}')
else:
    print(f'Errado! O número que eu estava pensando era {rand}')
