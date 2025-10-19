listagem = ('Frango', 15.00, 'Macarrão', 12.50, 'Pão', 5.00, 'Bolo', 10.65, 'Pastel', 7.50)
print('-'*45)
print(f'{'LISTAGEM DE PREÇOS':^45}')
print('-'*45)
for p in range(0, len(listagem), 2):
    print(f'{listagem[p]:.<36}R${listagem[p+1]:>7.2f}')
print(f'{'-'*45}')
