n1 = int(input('Digite o primeiro termo de uma PA: '))
R = int(input('Digite a razão dessa PA: '))
print('Os 10 primeiros termos dessa PA serão:')
i = 0
while i <= 9:
    print(f'{n1 + i * R} -> ', end='')
    i += 1
print('FIM')
