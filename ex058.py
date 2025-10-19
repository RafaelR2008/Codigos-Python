from random import randint
print('\033[34m=-=\033[m'*14)
print(f'{'\033[36mJOGO: ADIVINHE O NÚMERO V2.0\033[m':^51}')
print('\033[34m=-=\033[m'*14)
print('Pensarei em um número entre 0 e 10, você consegue adivinhar em que número estou pensando?')
cpu = randint(0, 10)
guess = int(input('\033[36mVocê está pensando no: '))
cont = 1
while guess != cpu:
    cont += 1
    print('\033[mErrado! Tente de novo')
    guess = int(input('\033[36mVocê está pensando no: '))
print(f'\033[mVocê acertou! Eu estava pensando no {cpu}')
if cont == 1:
    print(f'Foi apenas {cont} tentativa para você acertar, impressionante!')
else:
    print(f'Foram {cont} tentativas para você acertar, consegue fazer melhor?')
