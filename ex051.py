n1 = int(input('Digite o primeiro termo de uma PA: '))
R = int(input('Digite a razão dessa PA: '))
print('Os 10 primeiros termos dessa PA serão:')
for i in range(0,10):
    print(f'Termo {i + 1}: {n1 + (R * i)}')