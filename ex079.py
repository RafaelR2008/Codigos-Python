valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print('Valor adicionado com sucesso!')
        valores.append(valor)
    esc = input('Quer continuar? [S/N] ').strip().upper()
    while 'S' != esc != 'N':
        esc = input('Apenas S para sim ou N para não. Quer continuar? [S/N] ').strip().upper()
    if esc == 'N':
        break
print('=-'*20)
print(f'Você digitou os valores {sorted(valores)}')
