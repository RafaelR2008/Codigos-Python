dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
print(f'Ao alugar o carro por {dias} dias, e rodar por {km}Km, ', end='')
print(f'o preço a pagar será de: R${dias * 60 + km * 0.15:.2f}')