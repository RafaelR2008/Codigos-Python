c = 0
total = 0
a = 10
n1 = int(input('Digite o primeiro termo de uma PA: '))
R = int(input('Digite a razão dessa PA: '))
print('Os 10 primeiros termos dessa PA serão:')
while a != 0:
    total += a
    while c < total:
        print(f'{n1 + c * R} -> ', end='')
        c += 1
    print('PAUSA')
    a = int(input('Você quer que eu mostre mais quanto termos? '))
print(f'Progressão finalizada com {total} termos mostrados')
