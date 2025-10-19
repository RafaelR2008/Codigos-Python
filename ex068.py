from time import sleep
from random import randint
print('\033[31m-=-\033[m'*17)
print(f'\033[35m{'JOGO: PAR OU IMPAR?':^50}\033[m')
print('\033[31m-=-\033[m'*17)
cont = 0
while True:
    cpu = randint(0,10)
    num = int(input('Qual número você quer colocar? '))
    while num > 10 or num < 0:
        num = int(input('Digite apenas valores entre 0 e 10: '))
    mao = input('Par ou Impar? [P/I]  ').upper().strip()
    while 'P' != mao != 'I':
        mao = input('Escolha apenas P para par ou I para impar: ').upper().strip()
    print('-' * 30)
    print(f'Jogador: {num}')
    print(f'Computador: {cpu}')
    sleep(1)
    print('-'*30)
    paridade = ''
    if (num + cpu) % 2 == 0:
        print(f'{num} mais {cpu} é igual a {num + cpu}. Deu PAR ')
        paridade = 'P'
    else:
        print(f'{num} mais {cpu} é igual a {num + cpu}. Deu IMPAR ')
        paridade = 'I'
    sleep(1)
    print('-'*30)
    if paridade == mao:
        cont += 1
        print('Você venceu!\nVamos jogar de novo...')
        print('='*30)
    else:
        print(f'Você perdeu!\nVocê teve uma sequência de {cont} vitótias')
        break
