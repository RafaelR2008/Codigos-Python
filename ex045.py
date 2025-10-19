from time import sleep
from random import choice
print(f'{'\033[35m'}-=-'*20)
print(f'{'\033[32m'}{'PEDRA, PAPEL OU TESOURA?':^60}{'\033[m'}')
print(f'{'\033[35m'}-=-'*20+'\033[m')
jogadas = ['PEDRA','PAPEL','TESOURA']
cpu = choice(jogadas)
print('Tenho minha jogada em mente! Qual será a sua?')
player = int(input('1 - PEDRA\n2 - PAPEL\n3 - TESOURA\n'))
if player in [1,2,3]:
    player = jogadas[player - 1]
    print('Certo...vamos lá!')
    sleep(1)
    print('jo...')
    sleep(1)
    print('ken...')
    sleep(1)
    print('PO!!!')
    print(f'Jogador: {player}\t\tCpu: {cpu}')
    if player == cpu:
        print('\nEmpate!')
    else:
        if player == 'PEDRA':
            if cpu == 'PAPEL':
                print('\nHa! Eu ganhei!')
            else:
                print('\nPoxa, você me venceu!')
        elif player == 'PAPEL':
            if cpu == 'TESOURA':
                print('\nHa! Eu ganhei!')
            else:
                print('\nPoxa, você me venceu!')
        else:
            if cpu == 'PEDRA':
                print('\nHa! Eu ganhei!')
            else:
                print('\nPoxa, você me venceu!')
else:
    print('Escolha uma opção válida da próxima vez!')
