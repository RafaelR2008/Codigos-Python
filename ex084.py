pessoas = []
dados = []
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    esc = input('Quer continuar? [S/N] ').strip().upper()
    while 'S' != esc != 'N':
        esc = input('Apenas S para sim ou N para não. Quer continuar? [S/N] ').strip().upper()
    if esc == 'N':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
maior = menor = pessoas[0][1]
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO maior peso foi de {menor:.1f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
