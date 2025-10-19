sal = float(input('Qual o salário do funcionário? R$'))
if sal > 1250:
    print(f'Após o aumento, seu salário será de: R${sal*110/100:.2f}')
else:
    print(f'Após o aumento, seu salário será de: R${sal*115/100:.2f}')
