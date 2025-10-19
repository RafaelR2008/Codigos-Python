dist = float(input('Qual a distância da viagem em Km? '))
if dist > 200:
    print(f'Sua passagem irá custar R${dist * 0.45:.2f}')
else:
    print(f'Sua passagem irá custar R${dist * 0.50:.2f}')