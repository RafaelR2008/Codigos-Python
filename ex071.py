print('=-='*10)
print(f'{'CAIXA ELETRÔNICO SELF CASH':^30}')
print('=-='*10)
valor = int(input('Quanto você quer sacar? R$'))
while True:
    n50 = valor // 50
    valor -= 50 * n50
    if n50 > 0:
        print(f'Total de {n50} cédulas de R$50')
    if valor == 0:
        break
    n20 = valor // 20
    valor -= 20 * n20
    if n20 > 0:
        print(f'Total de {n20} cédulas de R$20')
    if valor == 0:
        break
    n10 = valor // 10
    valor -= 10 * n10
    if n10 > 0:
        print(f'Total de {n10} cédulas de R$10')
    if valor == 0:
        break
    n1 = valor // 1
    valor -= 1 * n1
    print(f'Total de {n1} cédulas de R$1')
    break
print('=-='*10)
print('Volte sempre ao CAIXA ELETRÔNICO SELF CASH! Tenha um bom dia!')
