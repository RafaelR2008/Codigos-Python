s = 0
print('Digite 6 números, e eu direi a soma dos valores pares digitados')
for i in range(0,6):
    n = int(input('Número: '))
    if n % 2 == 0:
        s += n
print(f'A soma é igual a: {s}')