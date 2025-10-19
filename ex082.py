valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um valor: ')))
    esc = input('Quer continuar? [S/N] ').strip().upper()
    while 'S' != esc != 'N':
        esc = input('Apenas S para sim ou N para não. Quer continuar? [S/N] ').strip().upper()
    if esc == 'N':
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
