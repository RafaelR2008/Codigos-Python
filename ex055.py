maior = 0
menor = 0
print('Digite o peso de 5 pessoas')
for i in range(0,5):
    p = float(input('Peso: '))
    if i == 0:
        maior = p
        menor = p
    if p > maior:
        maior = p
    if p < menor:
        menor = p
print(f'O maior peso digitado foi de {maior}Kg, e o menor foi de {menor}Kg.')
