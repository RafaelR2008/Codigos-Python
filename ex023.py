#por strings
"""num = "000" + input('Escreva um número inteiro entre 0 e 9999: ')
print(f'Unidade: {num[len(num)-1]}')
print(f'Dezena: {num[len(num)-2]}')
print(f'Centena: {num[len(num)-3]}')
print(f'Milhar: {num[len(num)-4]}')"""

#por inteiros
num = int(input('Escreva um número inteiro entre 0 e 9999: '))
print(f'Unidade: {num // 1 % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centena: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')
