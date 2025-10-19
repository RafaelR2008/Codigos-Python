nome = input('Qual é o seu nome? ')
print(f'Primeiro: {nome.split()[0]}')
print(f'Último: {nome.split()[len(nome.split())-1]}')
