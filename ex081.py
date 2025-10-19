valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    esc = input('Quer continuar? [S/N] ').strip().upper()
    while 'S' != esc != 'N':
        esc = input('Apenas S para sim ou N para não. Quer continuar? [S/N] ').strip().upper()
    if esc == 'N':
        break
valores.sort(reverse=True)
print('=-'*20)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista e está nas posições:', end=' ')
    for pos, valor in enumerate(valores):
        if valor == 5:
            print(f'{pos}...  ', end='')
else:
    print('O valor 5 não foi encontrado na lista!')
