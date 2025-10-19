pre = float(input('Qual o preço do produto? '))
cond = int(input("""Qual a condição de pagamento?
1 - Á vista no dinheiro/cheque
2 - Á vista no cartão
3 - 2X no cartão
4 - 3X ou mais no cartão
"""))
if cond == 1:
    print(f'Você terá 10% de desconto e o novo preço será de R${pre*90/100:.2f}')
elif cond == 2:
    print(f'Você terá 5% de desconto e o novo preço será de R${pre*95/100:.2f}')
elif cond == 3:
    print('Você comprará o produto pelo preço normal')
elif cond == 4:
    parc = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parc}X de R${pre*120/100/parc:.2f} com juros', end=', ')
    print(f'e irá custar R${pre*120/100:.2f}')
else:
    print('Você não escolheu nenhuma das opções disponíveis')
