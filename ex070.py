total = caro = barato = cont = 0
nomeBarato = ''
print(f'\033[35m{'-'*40:^30}\033[m')
print(f'\033[36m{'LOJA SELF CASH':^40}\033[m')
print(f'\033[35m{'-'*40:^30}\033[m')
while True:
    cont += 1
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: '))
    total += preco
    if preco > 1000:
        caro += 1
    if cont == 1 or preco < barato:
        barato = preco
        nomeBarato = nome
    print('-'*30)
    esc = input('Quer continuar? [S/N] ').strip().upper()
    while 'S' != esc != 'N':
        esc = input('Escreva apenas S para sim ou N para não: ').strip().upper()
    if esc == 'N':
        print(f'{'VOLTE SEMPRE!':=^30}')
        break
print(f'O total da compra foi de R${total:.2f}.')
print(f'Você comprou {caro} produtos que custam mais de R$1000.00.')
print(f'O produto mais barato comprado foi {nomeBarato} que custa R${barato:.2f}.')
